import aws_cdk as core
import aws_cdk.assertions as assertions

from stock_options_analytics_and_prediction.stock_options_analytics_and_prediction_stack import StockOptionsAnalyticsAndPredictionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in stock_options_analytics_and_prediction/stock_options_analytics_and_prediction_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StockOptionsAnalyticsAndPredictionStack(app, "stock-options-analytics-and-prediction")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
