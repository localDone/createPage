import uuid
from random import choice


#       select merchantaccount.id, merchantaccount.last4, merchantaccount.name
# 		from company join merchantaccount on company.id=merchantaccount.companyid
# 		where company.name='MRI' and merchantaccount.id is not null limit 10;

# Manually Generated Variables
date_time = '2021-07-29 03:12:58.288000'
merchantaccountid = "d43f45da-ef35-451a-85dd-289fd205e467"
value = '11.31'
transactionid = 'e1d4d286-2ae2-4f19-90f0-1284b749ae53'

# Auto Generated Variables
fundstransfer_id = uuid.uuid1()
record_id = uuid.uuid1()
confirmation_id = str(uuid.uuid4()).split('-')[0] + str(uuid.uuid4()).split('-')[2]
confirmation_id = 'FT_' + ''.join(choice((str.upper, str.lower))(c) for c in confirmation_id)

print(
    'INSERT INTO fundstransfer (id, createdate, merchantaccountid, amount, confirmationid, type, _id, record_id, system_date, last4, status, updatedate, processor)')
# Add .replace(', ', ',\n') to see in break-lines
print('VALUES('
      '\'{0}\', '
      '\'{1}\', '
      '\'{2}\', '
      '\'{3}\', '
      '\'{4}\', '
      '\'TYPE_FUNDS_TRANSFER\', '
      '\'{0}\', '
      '\'{5}\', '
      '\'{1}\', '
      '\'4321\', '
      '\'INPROCESS\', '
      '\'2021-04-10 03:11:58.288000\', '
      '\'PAYSAFE_CASH\');'.format(fundstransfer_id, date_time, merchantaccountid, value, confirmation_id, record_id)
      .replace(', ', ',\n'))

print('\n-- DOUBLE-CHECK record was created')
print('select * from fundstransfer where id = \'{0}\''.format(fundstransfer_id))
print('\n-- Change disbursementstatus to INPROCESS and fundtransferid to {0}'.format(fundstransfer_id))
print('select * from paymenttransaction where id = \'{0}\''.format(transactionid))

# print('-'.join(a + b for a, b in zip(uid.hex[0::1], uid.hex[1::2])))
