from faker import Faker


class BaseContact():
    def __init__(self, firstname, lastname, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.personalphone = phone
        self.personalemail = email

        #Variables
        #self._label_length = len(self.firstname + ' ' + self.lastname)

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.personalemail}'

    def __repr__(self):
        return f'firstname={self.firstname} lastname={self.lastname}'

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'.format(self.personalphone, self.firstname, self. lastname))

    @property
    def label_length(self):
        return len(self.firstname) + len(self.lastname) +1


class BusinessContact(BaseContact):
    def __init__(self, company, job, workemail, workphone,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.workemail = workemail
        self.workphone = workphone

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'.format(self.workphone, self.firstname, self. lastname))

# print(issubclass(BusinessContact, BaseContact))

# def generate_fake_names(type, qty):
#     basenames = []
#     businessnames = []
#     fake = Faker()
#     if type == 'base':
#         for i in range(qty):
#             basenames.append(BaseContact(firstname=fake.first_name(),\
#                 lastname=fake.last_name(),\
#                 phone=fake.phone_number(),\
#                 email=fake.email())
#             )
#     else:
#         for i in range(qty):
#             businessnames.append(BusinessContact(firstname=fake.first_name(),\
#                 lastname=fake.last_name(), phone=fake.phone_number(),\
#                 email=fake.email(), company=fake.company(),\
#                 job=fake.job(), workemail=fake.company_email(),\
#                 workphone=fake.phone_number())
#             )
#     return basenames, businessnames

def generate_fake_names(type, qty):
    # names = []
    fake = Faker()
    if type=='base':
        names = [BaseContact(firstname=fake.first_name(),\
            lastname=fake.last_name(),\
            phone=fake.phone_number(),\
            email=fake.email())\
            for i in range(qty) ]
    else:
        names = [BusinessContact(firstname=fake.first_name(),\
            lastname=fake.last_name(),\
            phone=fake.phone_number(),\
            email=fake.email(),\
            company=fake.company(),\
            job=fake.job(),\
            workemail=fake.company_email(),\
            workphone=fake.phone_number())
            for i in range(qty) if type=='business']
    return names


type = 'business'

namelist = generate_fake_names(type, 5)

if type == 'base':

    print('\nBase')
    print('---------------\n')

    for name in namelist:
        print('{} {} {} {}'.format(name.firstname, name.lastname, name.personalphone, name.personalemail))
        print(name.label_length)
        name.contact()
else:
    print('\nBusiness')
    print('---------------\n')

    for name in namelist:
        print('{} {} {} {} {}'.format(name.firstname, name.lastname, name.personalphone, name.workphone, name.workemail))
        print(name.label_length)
        name.contact()


# namelist_sorted_by_first_name = sorted(namelist, key=lambda name: name.firstname)
# namelist_sorted_by_last_name = sorted(namelist, key=lambda name: name.lastname)
# namelist_sorted_by_email = sorted(namelist, key=lambda name: name.email)
#
# for name in namelist_sorted_by_first_name:
#     print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
# print('\n')
# for name in namelist_sorted_by_last_name:
#     print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
# print('\n')
# for name in namelist_sorted_by_email:
#     print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
