from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

class StockPredictionStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Example: Create an S3 bucket
        bucket = s3.Bucket(self, "StockDataBucket", versioned=True)

        # Example: Create a Lambda function
        lambda_function = _lambda.Function(
            self, "DataFetcherLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_code"),
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }
        )
