# aws-cdk-starter

A production-shaped AWS CDK starter (Python) demonstrating a real-world serverless pattern — S3 → SQS → Lambda — with hardened defaults, pinned dependencies, and full unit-test coverage.

---

## Architecture

```
          ┌──────────┐      event source      ┌──────────────┐
          │  SQS     │ ─────────────────────► │  Lambda      │
          │  Queue   │                         │  (Python 3.12│
          └──────────┘                         │   handler)   │
                                               └──────┬───────┘
                                                      │ read
                                               ┌──────▼───────┐
                                               │   S3 Bucket  │
                                               │  (versioned, │
                                               │  private)    │
                                               └──────────────┘
```

| Resource | Config |
|---|---|
| S3 Bucket | Versioned, all public access blocked |
| SQS Queue | 300 s visibility timeout, 10-msg batch to Lambda |
| Lambda | Python 3.12, triggered by SQS, reads from S3 |

---

## Prerequisites

- Python 3.12+
- Node.js 18+ (required by CDK CLI)
- AWS CDK v2: `npm install -g aws-cdk`
- AWS credentials configured (`aws configure` or env vars)

---

## Quick start

```bash
cd cdk_src
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
pip install -r requirements-dev.txt

# Synthesize the CloudFormation template
cdk synth

# Deploy to your AWS account
cdk deploy
```

---

## Running tests

```bash
cd cdk_src
pytest tests/ -v
```

---

## Project layout

```
aws-cdk-starter/
├── cdk_src/
│   ├── app.py                    # CDK app entry point
│   ├── cdk.json                  # CDK toolkit config
│   ├── requirements.txt          # Runtime dependencies (pinned)
│   ├── requirements-dev.txt      # Test dependencies (pinned)
│   ├── cdk_src/
│   │   └── cdk_src_stack.py      # Stack definition (S3 + SQS + Lambda)
│   ├── lambda/lambda/
│   │   └── hello_lambda.py       # Lambda handler
│   └── tests/unit/
│       └── test_cdk_src_stack.py # CDK assertions unit tests
```

---

*Built by Ascent DevOps · Veteran-Owned · SDVOSB*
