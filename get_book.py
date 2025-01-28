import boto3
from botocore.exceptions import ClientError

def get_book(book_id, title, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    books_table = dynamodb.Table('Books')

    try:
        response = books_table.get_item(
            Key={'book_id': book_id, 'title': title})
    except ClientError as e:
            print(e.response['No item found'])
    else:
            return response['Item']

if __name__ == '__main__':
    book = get_book(1000, "Atomic habits")
    if book:
        print(book)
