from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import vobject
import phonenumbers

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Tambahkan widget untuk input nama dan nomor telepon
        self.name_input = TextInput(hint_text='Masukkan Nama')
        self.add_widget(self.name_input)
        self.phone_input = TextInput(hint_text='Masukkan Nomor Telepon')
        self.add_widget(self.phone_input)

        # Tambahkan tombol untuk mengkonversi ke VCF
        self.convert_button = Button(text='Konversi ke VCF')
        self.convert_button.bind(on_press=self.convert_to_vcf)
        self.add_widget(self.convert_button)

        # Tambahkan tombol untuk split VCF
        self.split_button = Button(text='Split VCF')
        self.split_button.bind(on_press=self.split_vcf)
        self.add_widget(self.split_button)

        # Tambahkan tombol untuk mengubah nama dalam VCF
        self.change_name_button = Button(text='Ubah Nama')
        self.change_name_button.bind(on_press=self.change_name)
        self.add_widget(self.change_name_button)

        # Tambahkan tombol untuk mengkonversi VCF ke TXT
        self.convert_vcf_to_txt_button = Button(text='Konversi VCF ke TXT')
        self.convert_vcf_to_txt_button.bind(on_press=self.convert_vcf_to_txt)
        self.add_widget(self.convert_vcf_to_txt_button)

        # Tambahkan tombol untuk admin
        self.admin_button = Button(text='Admin')
        self.admin_button.bind(on_press=self.admin_mode)
        self.add_widget(self.admin_button)

    def convert_to_vcf(self, instance):
        # Fungsi untuk mengkonversi ke VCF
        name = self.name_input.text
        phone_number = self.phone_input.text
        try:
            x = phonenumbers.parse(phone_number)
            formatted_phone_number = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            vcard = vobject.vCard()
            vcard.add('fn').value = name
            vcard.add('tel').value = formatted_phone_number
            # Simpan vcard ke file
            with open('output.vcf', 'w') as f:
                f.write(vcard.serialize())
        except Exception as e:
            print(f"Error: {e}")

    def split_vcf(self, instance):
        # Fungsi untuk split VCF
        # ...

    def change_name(self, instance):
        # Fungsi untuk mengubah nama dalam VCF
        # ...

    def convert_vcf_to_txt(self, instance):
        # Fungsi untuk mengkonversi VCF ke TXT
        # ...

    def admin_mode(self, instance):
        # Fungsi untuk mode admin
        self.admin_layout = BoxLayout(orientation='vertical')
        self.admin_name_input = TextInput(hint_text='Masukkan Nama Admin')
        self.admin_layout.add_widget(self.admin_name_input)
        self.admin_phone_input = TextInput(hint_text='Masukkan Nomor Admin')
        self.admin_layout.add_widget(self.admin_phone_input)
        self.navy_name_input = TextInput(hint_text='Masukkan Nama Navy')
        self.admin_layout.add_widget(self.navy_name_input)
        self.navy_phone_input = TextInput(hint_text='Masukkan Nomor Navy')
        self.admin_layout.add_widget(self.navy_phone_input)
        self.save_button = Button(text='Simpan')
        self.save_button.bind(on_press=self.save_admin_data)
        self.admin_layout.add_widget(self.save_button)
        self.add_widget(self.admin_layout)

    def save_admin_data(self, instance):
        # Fungsi untuk menyimpan data admin
        admin_name = self.admin_name_input.text
        admin_phone = self.admin_phone_input.text
        navy_name = self.navy_name_input.text
        navy_phone = self.navy_phone_input.text
        # Simpan data ke file atau database
        print(f"Admin Name: {admin_name}, Admin Phone: {admin_phone}, Navy Name: {navy_name}, Navy Phone: {navy_phone}")

class Xiaomei_Convert(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    Xiaomei_Convert().run()
