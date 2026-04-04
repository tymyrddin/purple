# Terraform vulnerable lab template

## Setup

```hcl
# main.tf
provider "aws" {
  region = "us-east-1"
}

provider "google" {
  credentials = file("gcp-creds.json")
  project     = "your-project-id"
  region      = "us-central1"
}

resource "random_id" "suffix" {
  byte_length = 4
}
```

## Beginner: "The Oversharing Bucket" (AWS S3)

Goal: find an open S3 bucket and retrieve flag.txt.

```hcl
resource "aws_s3_bucket" "beginner" {
  bucket = "rootme-beginner-${random_id.suffix.hex}"
  acl    = "public-read"  # deliberately misconfigured

  tags = {
    Name = "Flag Storage"
  }
}

resource "aws_s3_bucket_object" "flag" {
  bucket  = aws_s3_bucket.beginner.id
  key     = "flag.txt"
  content = "FLAG: S3_Leak_${random_id.suffix.hex}"
}
```

Solution:

```bash
aws s3 ls s3://rootme-beginner-[ID] --no-sign-request
aws s3 cp s3://rootme-beginner-[ID]/flag.txt - --no-sign-request
```

Fix: `acl = "private"`

## Intermediate: "Lambda to EC2 Takeover" (AWS IAM)

Goal: from Lambda, steal IAM keys to access EC2.

```hcl
resource "aws_iam_role" "lambda" {
  name = "overprivileged_lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_admin" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"  # deliberately overprivileged
}

resource "aws_lambda_function" "vulnerable" {
  filename      = "lambda.zip"
  function_name = "leaky_lambda"
  role          = aws_iam_role.lambda.arn
  handler       = "index.handler"
  runtime       = "python3.8"
  environment {
    variables = {
      FLAG = "Lambda_Key_${random_id.suffix.hex}"
    }
  }
}

resource "aws_instance" "target" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "Flag_EC2"
  }
}
```

Solution:

```bash
# dump Lambda env vars, then:
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
aws ec2 describe-instances --region us-east-1
```

Fix: `policy_arn = "arn:aws:iam::aws:policy/AWSLambdaBasicExecutionRole"`

## Advanced: "GCP Org Compromise" (service account key)

Goal: use a leaked key to escalate to project owner.

```hcl
resource "google_service_account" "leaky" {
  account_id   = "leaky-sa-${random_id.suffix.hex}"
  display_name = "Leaky Service Account"
}

resource "google_project_iam_member" "owner" {
  project = "your-project-id"
  role    = "roles/owner"  # deliberately overprivileged
  member  = "serviceAccount:${google_service_account.leaky.email}"
}

resource "google_service_account_key" "leaky_key" {
  service_account_id = google_service_account.leaky.name
  public_key_type    = "TYPE_X509_PEM_FILE"
}

output "leaky_key_json" {
  value     = google_service_account_key.leaky_key.private_key
  sensitive = true
}
```

Solution:

```bash
echo "$LEAKED_KEY_JSON" > creds.json
gcloud auth activate-service-account --key-file=creds.json
gcloud projects get-iam-policy your-project-id
gcloud compute instances list
```

Fix: `role = "roles/logging.viewer"`

## Deploy

```bash
terraform init
terraform apply -auto-approve
# after CTF:
terraform destroy -auto-approve
```
