from django.contrib import admin
from .models import Transaksi, DetailTransaksi


# class DataTransaksiAdmin(admin.ModelAdmin):
#     list_display = ("no_transaksi", "nama_depan", "nama_belakang", "alamt", "provinsi", "kabupaten", "kecamatan",
#                     "kode_post", "email", "whatsapp", "total_transaksi", "status", "date_created", "tanggal_kirim")


# class DataDetailTransaksiAdmin(admin.ModelAdmin):
#     list_display = ("no_transaksi", "produk", "jumlah")


admin.site.register(Transaksi)
admin.site.register(DetailTransaksi)
