from aws_cdk.aws_lambda import (
    Runtime,
    Code
)

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_events,
    Duration,
)

from constructs import Construct

class CdkSrcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

    #Create s3 bucket
        bucket = s3.Bucket(self, "MyBucket",
            bucket_name='corriere-test',
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

    #Create a SQS
        queue = sqs.Queue(self, 'MyQueue',
            queue_name="corriere-test-queue",
            visibility_timeout=Duration.seconds(300)
        )

    #Create a Lambda Function
        my_lambda = _lambda.Function(self, "MyLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="hello_lambda.handler",
            code=Code.from_asset("lambda")
        )

        # Wire SQS as the Lambda trigger
        my_lambda.add_event_source(
            lambda_events.SqsEventSource(queue, batch_size=10)
        )

        # Grant Lambda read access to the S3 bucket
        bucket.grant_read(my_lambda)