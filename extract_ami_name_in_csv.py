import boto3,csv
ec2 = boto3.client('ec2', region_name='us-east-1')
owner_id = 'XXXXXXXXXX'
filters = [{'Name': 'owner-id', 'Values': [owner_id]}]
response = ec2.describe_images(Filters=filters)
with open('instance_images_us-east-1.csv', 'w') as csvfile:
	fieldnames = ['Image_Id','Name','ImageLocation','CreationDate']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for image in response['Images']:
			print(image['ImageId'])
			print(image['Name'])
			print(image['ImageLocation'])
			print(image['CreationDate'])
			print(image)
			writer.writerow({'Image_Id': image['ImageId'], 'Name': image['Name'], 'ImageLocation': image['ImageLocation'], 'CreationDate': image['CreationDate'] })
