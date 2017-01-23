https://www.hackster.io/bees/aws-iot-and-beehives-c59fff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--
-- create DynamoDB table
--
aws dynamodb create-table \
	--table-name foobar1 \
	--attribute-definitions \
			AttributeName=foo,AttributeType=S \
			AttributeName=bar,AttributeType=S  \
	--key-schema \
			AttributeName=foo,KeyType=HASH \
			AttributeName=bar,KeyType=RANGE \
	--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

	"arn:aws:dynamodb:us-west-2:123275298972:table/foobar1"

-- create role 
cat > foobar-role.txt
{  
  "Version":"2012-10-17",
  "Statement":[  
    {  
      "Sid":"",
      "Effect":"Allow",
      "Principal":{  
        "Service":"iot.amazonaws.com"
      },
      "Action":"sts:AssumeRole"
    }
  ]
}

aws iam create-role --role-name "foobar-role" --assume-role-policy-document file://foobar-role.txt
	"arn:aws:iam::123275298972:role/foobar-role"

-- create policy (for accessing dynamoDB)
cat > foobar-policy.txt
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:*"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-west-2:123275298972:table/foobar1"
            ]
        }
    ]
}

aws iam create-policy --policy-name "foobar-policy" --policy-document file://foobar-policy.txt
	"arn:aws:iam::123275298972:policy/foobar-policy"

-- attach policy to role
aws iam attach-role-policy --role-name "foobar-role" --policy-arn "arn:aws:iam::123275298972:policy/foobar-policy"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--
-- basic rule
--
cat > foobar-rule.txt
{  
  "sql":"SELECT * FROM 'topic/foobar/data'",
  "ruleDisabled":false,
  "actions":[  
    {  
      "dynamoDB":{  
        "tableName":"foobar1",
        "hashKeyField":"foo",
        "hashKeyValue":"${clientId()}",
        "rangeKeyField":"bar",
        "rangeKeyValue":"${timestamp()}",
        "roleArn":"arn:aws:iam::123275298972:role/foobar-role"
      }
    }
  ]
}

aws iot create-topic-rule --rule-name "foobar_rule" --topic-rule-payload  file://foobar-rule.txt

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- test sending data through mosquitto client
apt-get install mosquitto-clients

mosquitto_pub \
	--cafile ../ssl/root-CA.crt \
	--cert ../ssl/cert.pem \
	--key ../ssl/privkey.pem \
	-h a1arqmop0meczp.iot.us-west-2.amazonaws.com \
	-p 8883 -q 1 -d \
	-t "topic/foobar/data" \
	-i foobar123 \
	-m "{\"foo\": \"foo2\",  \"bar\": \"bar2\"}"



