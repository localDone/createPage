import uuid
from random import choice
import datetime

#       select merchantaccount.id, merchantaccount.last4, merchantaccount.name
# 		from company join merchantaccount on company.id=merchantaccount.companyid
# 		where company.name='MRI' and merchantaccount.id is not null limit 10;

# Manually Generated Variables
transaction_id = '91a95ff2-5977-490e-a452-464b55e68185'
eft_amount = '37.31'


# Automatically Generated Variables
open_symbol = '\n{\n'

close_symbol = '\n}'
message_type = 'EFT'
settlement_date = str(datetime.datetime.now()).replace(' ', 'T').split('.')[0] + '+0000'
new_date = settlement_date.split('+')[0].replace('T', '_').replace('-', '').replace(':', '')
file = 'AMR_Transaction_Reconciliation_103792_PROPERTII_Rentmoola_{0}.csv'.format(new_date)



def create_BCC_EFT():
      # Manually Generated Variables
      merchant_account = "1001689880"

      # Automatically Generated Variables
      payment_type = 'BCC_'
      confirmation_id = str(uuid.uuid4()).split('-')[0] + str(uuid.uuid4()).split('-')[2]
      confirmation_id = payment_type + ''.join(choice((str.upper, str.lower))(c) for c in confirmation_id)
      processor = 'PAYSAFE_SPLIT_PAY'
      create_EFT = open_symbol + '|message_type|:|{0}|,\n' \
                                 '|confirmation_id|:|{1}|,\n' \
                                 '|settlement_date|:|{2}|,\n' \
                                 '|eft_amount|:|{3}|,\n' \
                                 '|merchant_account|:|{4}|,\n' \
                                 '|processor|:|{5}|,\n' \
                                 '|file|:|{6}|' \
            .format(message_type, confirmation_id, settlement_date, eft_amount, merchant_account, processor, file) \
            .replace('|', '\"') + close_symbol

      print(create_EFT)
      push_eft_string = open_symbol + '|message_type|:|{0}|,\n' \
                                 '|confirmation_id|:|{1}|,\n' \
                                 '|transactions|:[' \
                                      '{2}' \
                                      '|transaction_type|:|{3}|,\n' \
                                 '|id|:|{4}|,\n' \
                                 '|settlement_date|:|{5}|{6}\n]' \
            .format('EFTDETAIL', confirmation_id, open_symbol, "PAYMENT", transaction_id, settlement_date, close_symbol) \
            .replace('|', '\"') + close_symbol
      print(push_eft_string)





def create_PPL_EFT():
      # Manually Generated Variables
      merchant_account = "4H6LXD4RFFXE8"

      # Automatically Generated Variables
      payment_type = 'PAYPAL_'
      confirmation_id = str(uuid.uuid4()).split('-')[0] + str(uuid.uuid4()).split('-')[2]
      confirmation_id = payment_type + ''.join(choice((str.upper, str.lower))(c) for c in confirmation_id)
      processor = 'PAY_PAL'
      create_EFT = open_symbol + '|message_type|:|{0}|,\n' \
                                 '|confirmation_id|:|{1}|,\n' \
                                 '|settlement_date|:|{2}|,\n' \
                                 '|eft_amount|:|{3}|,\n' \
                                 '|merchant_account|:|{4}|,\n' \
                                 '|processor|:|{5}|,\n' \
                                 '|file|:|{6}|' \
            .format(message_type, confirmation_id, settlement_date, eft_amount, merchant_account, processor, file) \
            .replace('|', '\"') + close_symbol

      print(create_EFT)
      push_eft_string = open_symbol + '|message_type|:|{0}|,\n' \
                                 '|confirmation_id|:|{1}|,\n' \
                                 '|transactions|:[' \
                                      '{2}' \
                                      '|transaction_type|:|{3}|,\n' \
                                 '|id|:|{4}|,\n' \
                                 '|settlement_date|:|{5}|{6}\n]' \
            .format('EFTDETAIL', confirmation_id, open_symbol, "PAYMENT", transaction_id, settlement_date, close_symbol) \
            .replace('|', '\"') + close_symbol
      print(push_eft_string)


create_BCC_EFT()
# create_PPL_EFT()

