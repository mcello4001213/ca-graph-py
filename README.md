# Block Access ke Microsoft / Office 365 pada Waktu Tertentu saja

Solusi ini untuk membatasi akses ke Microsoft / Office 365 di Periode waktu tertentu saja menggunakan Python - Graph API - Cron Job / Crontab 

# Prerequisites
• Mempunyai Application yang terdaftar di Azure AD -> <a href = "https://docs.microsoft.com/en-us/graph/auth-register-app-v2" target="_blank">Tentang Register App</a>

• Application yang terdaftar di Azure AD sudah mempunyai izin untuk menggunakan Graph API -> <a href = "https://github.com/Azure-Samples/azure-ad-conditional-access-apis/blob/main/01-configure/graphapi/readme.md" target="_blank">Tentang Perizinan API Conditional Access</a>

# Install Module, Config file, modify with your data and credentials before running the script
• Install Modul -> 'requests' di Python anda

• Ubah variabel yang berada di dalam file dan sesuaikan dengan data yang anda punya

# Images of how script works

<img src="screenshots/post.PNG"><br>
<img src="screenshots/post-ca.PNG"><br>
<img src="screenshots/delete.PNG"><br>
<img src="screenshots/delete-ca.PNG"><br>

