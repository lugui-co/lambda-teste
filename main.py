import json

def lambda_handler(event, context):
    try:
        # Parse the input event
        body = json.loads(event.get('body', '{}'))
        
        # Process the request
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'data': body
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
        return response
        
    except Exception as e:
        # Handle errors
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error',
                'error': str(e)
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
