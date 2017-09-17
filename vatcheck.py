import zeep
import argparse
import re


def main():
    parser = argparse.ArgumentParser(description='Check VAT number using VIES')
    parser.add_argument('vat_number', help='The VAT number to be checked', metavar='VAT')
    args = parser.parse_args()

    match = re.search(r'([A-Z]{2})([0-9A-Za-z\+\*\.]{2,12})', args.vat_number)

    if match:
        try:
            wsdl = 'http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl'
            client = zeep.Client(wsdl=wsdl)
            service = client.bind('checkVatService', 'checkVatPort')
            result = service.checkVat(match.group(1), match.group(2))
            if result['valid']:
                print 'Valid'
            else:
                print 'Invalid'
        except Exception as e:
            print 'Error processing the request: ', e
    else:
        print 'Invalid parameter: ', args.vat_number


if __name__ == '__main__':
    main()
