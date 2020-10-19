from faker import Faker


class BaseContact():
    def __init__(self, firstname, lastname, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.personalphone = phone
        self.personalemail = email

        #Variables
        self._label_length = len(self.firstname + ' ' + self.lastname)

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.email}'

    def __repr__(self):
        return f'firstname={self.firstname} lastname={self.lastname} company={self.company} post={self.post} email={self.email}'

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'.format(self.personalphone, self.firstname, self. lastname))

    @property
    def label_length(self):
        return self._label_length


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

def generate_fake_names(type, qty):
    basenames = []
    businessnames = []
    fake = Faker()
    if type == 'base':
        for i in range(qty):
            basenames.append(BaseContact(firstname=fake.first_name(),\
                lastname=fake.last_name(),\
                phone=fake.phone_number(),\
                email=fake.email())
            )
    else:
        for i in range(qty):
            businessnames.append(BusinessContact(firstname=fake.first_name(),\
                lastname=fake.last_name(), phone=fake.phone_number(),\
                email=fake.email(), company=fake.company(),\
                job=fake.job(), workemail=fake.company_email(),\
                workphone=fake.phone_number())
            )
    return basenames, businessnames


basenamelist, businessnamelist = generate_fake_names('business', 5)

print('\nBase')
print('---------------\n')

for name in basenamelist:
    print('{} {} {} {}'.format(name.firstname, name.lastname, name.personalphone, name.personalemail))
    print(name.label_length)
    print(name.contact())

print('\nBusiness')
print('---------------\n')

for name in businessnamelist:
    print('{} {} {} {} {}'.format(name.firstname, name.lastname, name.personalphone, name.workphone, name.workemail))
    print(name.label_length)
    print(name.contact())



print('\n')

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
