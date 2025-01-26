import os  # Import the os module
from aws_cdk import App, Environment
from stock_options_analytics_and_prediction.stock_options_analytics_and_prediction_stack import StockPredictionStack

# Initialize the CDK App
app = App()

# Add the stack
# Specify environment directly
StockPredictionStack(
    app,
    "StockOptionsAnalyticsAndPredictionStack",
    env=Environment(
        account="808505342526",  # Replace with your AWS account ID
        region="us-east-1"      # Replace with your desired region
    )
)

# Synthesize the app
app.synth()
