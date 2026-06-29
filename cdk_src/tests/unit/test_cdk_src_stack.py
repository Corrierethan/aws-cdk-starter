import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_src.cdk_src_stack import CdkSrcStack


def _template():
    app = core.App()
    stack = CdkSrcStack(app, "cdk-src")
    return assertions.Template.from_stack(stack)


def test_sqs_queue_created():
    template = _template()
    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_s3_bucket_versioning_enabled():
    template = _template()
    template.has_resource_properties("AWS::S3::Bucket", {
        "VersioningConfiguration": {"Status": "Enabled"}
    })


def test_s3_bucket_blocks_public_access():
    template = _template()
    template.has_resource_properties("AWS::S3::Bucket", {
        "PublicAccessBlockConfiguration": {
            "BlockPublicAcls": True,
            "BlockPublicPolicy": True,
            "IgnorePublicAcls": True,
            "RestrictPublicBuckets": True,
        }
    })


def test_lambda_runtime_is_python312():
    template = _template()
    template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.12"
    })


def test_lambda_sqs_event_source_mapping():
    template = _template()
    template.resource_count_is("AWS::Lambda::EventSourceMapping", 1)