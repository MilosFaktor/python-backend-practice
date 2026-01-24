# validate and build sam
sam validate
sam build

# sam local invoke LambdaA /get
sam local invoke LambdaAFunction

# creating local dynamodb
docker run -p 8000:8000 amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb # shared DB


aws dynamodb create-table \
    --table-name IdempotencyTable \
    --attribute-definitions AttributeName=request_id,AttributeType=S \
    --key-schema AttributeName=request_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --endpoint-url http://localhost:8000



# sam local invoke lambda b /post  with env.json and event.json
sam local invoke LambdaBFunction --event events/event.json --env-vars events/env.json


# local invoke API
sam local start-api --env-vars events/env.json

# scan local dynamoDB
aws dynamodb scan --table-name IdempotencyTable --endpoint-url http://localhost:8000



# running my local_client.py for local env reading from .env.local
python3 local_client.py

# running my local_client.py for my dev online env
ENV=dev python local_client.py


# aliases
alias run-local="python3 local_client.py"
alias run-dev="ENV=dev python3 local_client.py"
alias scan-local-table="aws dynamodb scan --table-name IdempotencyTable --endpoint-url http://localhost:8000"


# fast commands
run-local   # run local env
run-dev   # run dev env
scan-local-table   # scan local table

# accessing aliases
alias

# delete alias
unalias <alias_name>

# removing aliases
unalias run-local
unalias run-dev
unalias scan-table

# deploying sam
sam deploy --guided

# alias dynamoDB
alias scan-table="aws dynamodb scan --table-name http-ingest-validate-IdempotencyTable-1V6N0AOZC9OQT"


# local stack exec
run-local
scan-local-table


# online stack exec
run-dev
scan-table

# delete stack
sam delete --stack-name http-ingest-validate
