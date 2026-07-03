import streamlit as st
import streamlit.components.v1 as components
import base64

# ۱. تنظیمات اولیه صفحه استریم‌لیت
st.set_page_config(
    page_title="Soodo Tax",
    page_icon="💰",
    layout="wide"
)

# حذف فاصله خالی پیش‌فرض بالای صفحه در استریم‌لیت
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.2rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        header {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# تابع تبدیل عکس به Base64
def image_to_base64(path):
    try:
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        return ""

# تابع تبدیل فونت به Base64
def font_to_base64(path):
    try:
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()
    except FileNotFoundError:
        return ""

# لود کردن فایل‌ها از پوشه پروژه شما
logo_base64 = image_to_base64("logo.png")
calc_base64 = image_to_base64("hero.png")
font_base64 = font_to_base64("IRANYekan.ttf")


# =========================================================
# ۲. بخش هدر سایت (Navbar) - نسخه هوشمند با هدف اینستاگرام
# =========================================================
components.html(f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@font-face {{
    font-family: 'IRANYekan';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

* {{
    font-family: 'IRANYekan', Tahoma, sans-serif;
    box-sizing: border-box;
}}

body {{
    margin: 0;
    background: white;
    overflow: hidden;
}}

.navbar {{
    width: 100%;
    height: 95px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 70px;
    border-bottom: 1px solid #e5e7eb;
    background: white;
    direction: ltr; /* منو راست، برند چپ */
}}

.brand {{
    display: flex;
    align-items: center;
    gap: 15px;
    direction: ltr;
}}

.brand-text {{
    text-align: right;
}}

.brand img {{
    width: 120px;
    height: auto;
}}

.brand-title {{
    font-size: 26px;
    font-weight: 900;
    color: #111;
    line-height: 1.2;
}}

.brand-subtitle {{
    font-size: 13px;
    color: #555;
    margin-top: 4px;
}}

.menu {{
    display: flex;
    align-items: center;
    gap: 40px;
    direction: rtl;
}}

.menu a {{
    text-decoration: none;
    color: #222;
    font-size: 18px;
    font-weight: 600;
    padding-bottom: 5px;
    transition: color 0.2s;
}}

.menu a:hover {{
    color: #0f8f45;
}}

.menu a.active {{
    color: #0f8f45;
    border-bottom: 3px solid #0f8f45;
    padding-bottom: 18px; /* هماهنگی خط زیرین با پدینگ اصلی نوبار */
}}

/* استایل متمایز و کپسولی برای دکمه اینستاگرام */
.instagram-btn {{
    background: linear-gradient(135deg, #f9ce34 0%, #ee2a7b 50%, #6228d7 100%);
    color: white !important;
    padding: 10px 24px !important;
    border-radius: 50px;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0px 4px 15px rgba(238, 42, 123, 0.2);
    transition: transform 0.2s, box-shadow 0.2s !important;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: none !important; /* حذف خط زیرین منوهای عادی */
}}

.instagram-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0px 6px 20px rgba(238, 42, 123, 0.35);
    color: white !important;
}}

@media (max-width: 768px) {{
    .navbar {{
        padding: 0 20px;
        height: auto;
        min-height: 95px;
    }}
    .menu {{
        gap: 20px;
    }}
    .instagram-btn {{
        padding: 8px 16px !important;
        font-size: 14px !important;
    }}
}}
</style>
</head>

<body>
    <div class="navbar">
        <div class="brand">
            {"<img src='data:image/png;base64," + logo_base64 + "'>" if logo_base64 else ""}
            <div class="brand-text">
                <div class="brand-title">سودو آکادمی</div>
                <div class="brand-subtitle">ابزارهای کاربردی مالی و اکسل</div>
            </div>
        </div>

        <div class="menu">
            <a href="#" class="active" target="_top">خانه</a>
            
            <!-- دکمه اینستاگرام با لینک مستقیم شما (جایگزین آدرس اینستاگرامت کن رفیق) -->
            <a href="https://instagram.com/soodoacademy" class="instagram-btn" target="_blank">
                📸 اینستاگرام ما
            </a>
        </div>
    </div>
</body>
</html>
""", height=110)

# =========================================================
# ۳. بخش معرفی (Hero Section) - اصلاح فاصله کادر سبز
# =========================================================
components.html(f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@font-face {{
    font-family: 'IRANYekan';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}

* {{
    font-family: 'IRANYekan', Tahoma, sans-serif;
    box-sizing: border-box;
}}

body {{
    margin: 0;
    background: transparent;
    overflow-x: hidden;
}}

.hero-section {{
    display: flex;
    align-items: center;
    justify-content: center; /* تغییر به سنتر برای جمع شدن المان‌ها در وسط صفحه */
    padding: 20px 5%;
    gap: 80px; /* ایجاد یک فاصله منطقی و منظم بین کادر سبز و متن اصلی */
}}

.hero-left {{
    max-width: 500px; /* محدود کردن عرض برای تمرکز بیشتر متن */
    text-align: right;
}}

.hero-right {{
    display: flex;
    justify-content: center;
    align-items: center;
}}

.hero-right img {{
    width: 100%;
    max-width: 450px;
    height: auto;
}}

.hero-title {{
    font-size: 32px;
    font-weight: 900;
    color: #1e293b;
    line-height: 1.5;
    margin: 0 0 15px 0;
}}

.hero-title span {{
    color: #0f8f45;
}}

.hero-subtitle {{
    font-size: 16px;
    color: #64748b;
    line-height: 1.8;
    margin: 0 0 25px 0;
}}

.features-container {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.feature-box {{
    display: flex;
    align-items: center;
    gap: 6px;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 8px 14px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 600;
    color: #334155;
    white-space: nowrap;
}}

.hero-info-card {{
    width: 100%;
    max-width: 310px; /* فیکس کردن اندازه کادر سبز راهنما */
    background-color: #f4fbf7;
    border: 1px dashed #0f8f45;
    border-radius: 16px;
    padding: 20px;
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 10px;
}}

.info-card-title {{
    font-size: 16px;
    font-weight: 800;
    color: #0f8f45;
    display: flex;
    align-items: center;
    gap: 6px;
}}

.info-card-text {{
    font-size: 14px;
    color: #475569;
    line-height: 1.7;
}}

@media (max-width: 992px) {{
    .hero-section {{
        flex-direction: column;
        text-align: center;
        padding: 30px 20px;
        gap: 25px;
    }}
    .hero-left, .hero-right, .hero-info-card {{
        width: 100%;
        max-width: 600px;
        text-align: center;
    }}
    .features-container {{
        justify-content: center;
    }}
}}
</style>
</head>
<body>
    <div class="hero-section">
        <!-- ستون سمت راست: تصویر هیرو -->
        <div class="hero-right">
            {"<img src='data:image/png;base64," + calc_base64 + "'>" if calc_base64 else ""}
        </div>

        <!-- ستون وسط: متن‌ها و ویژگی‌ها -->
        <div class="hero-left">
            <h1 class="hero-title">محاسبه‌گر سریع و تخمینی<br><span>مالیات حقوق</span></h1>
            <p class="hero-subtitle">برآورد مالیات حقوق بر اساس قوانین جاری،<br>قبل از ارسال لیست حقوق</p>
            
            <div class="features-container">
                <div class="feature-box">🛡️ رایگان و امن</div>
                <div class="feature-box">⚡ محاسبه لحظه‌ای</div>
                <div class="feature-box">✅ سریع و دقیق</div>
            </div>
        </div>

        <!-- ستون سمت چپ: کادر سبز راهنما که حالا مهار شده -->
        <div class="hero-info-card">
            <div class="info-card-title">
                💡 این ابزار چیست؟
            </div>
            <div class="info-card-text">
                این ابزار برای برآورد سریع مالیات حقوق بر اساس جدول مالیاتی سال جاری طراحی شده است. نتیجه نهایی پس از ارسال لیست در سامانه سازمان امور مالیاتی محاسبه و اعلام می‌شود.
            </div>
        </div>
    </div>
</body>
</html>
""", height=390)

# =========================================================
# ۵. بخش فرم محاسبات (نسخه ۱۰۰٪ ریسپانسیو و هوشمند)
# =========================================================
components.html(f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@font-face {{
    font-family: 'IRANYekan';
    src: url(data:font/ttf;base64,{font_base64}) format('truetype');
}}
* {{
    font-family: 'IRANYekan', Tahoma, sans-serif;
    box-sizing: border-box;
}}
body {{
    margin: 0;
    background-color: transparent;
    overflow: hidden;
}}
.tax-card {{
    background-color: white;
    border-radius: 24px;
    box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.04);
    border: 1px solid #f1f5f9;
    padding: 30px 20px;
    margin: -20px auto 10px auto;
    width: 92%;
    max-width: 700px;
    text-align: center;
    position: relative;
    min-height: 290px;
}}
.tax-card-title {{
    font-size: 22px;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}}
.tax-card-subtitle {{
    font-size: 14px;
    color: #64748b;
    margin-bottom: 25px;
    padding: 0 10px;
    line-height: 1.6;
}}
.input-container {{
    display: flex;
    align-items: center;
    border: 2px solid #0f8f45;
    border-radius: 16px;
    overflow: hidden;
    width: 100%;
    max-width: 550px;
    margin: 0 auto 12px auto;
    background-color: white;
}}
.currency-label {{
    background-color: #f8fafc;
    border-right: 1px solid #e2e8f0;
    padding: 15px 20px;
    font-size: 16px;
    font-weight: bold;
    color: #1e293b;
}}
.amount-input {{
    flex: 1;
    border: none;
    padding: 15px 10px;
    font-size: 20px;
    font-weight: 700;
    color: #334155;
    text-align: center;
    outline: none;
    width: 100%;
}}
.input-help-text {{
    font-size: 13px;
    color: #64748b;
    margin-bottom: 15px;
}}
.calc-button {{
    background: linear-gradient(180deg, #0f8f45 0%, #0a6b33 100%);
    color: white;
    font-size: 18px;
    font-weight: 800;
    border: none;
    border-radius: 16px;
    padding: 15px 0;
    width: 100%;
    max-width: 550px;
    margin: 0 auto;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    box-shadow: 0px 8px 20px rgba(15, 143, 69, 0.3);
}}
.modal-overlay {{
    display: none;
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(255, 255, 255, 0.96);
    border-radius: 24px;
    z-index: 99;
    align-items: center;
    justify-content: center;
    padding: 20px;
}}
.modal-box {{
    max-width: 500px;
    width: 100%;
    animation: popupAnim 0.25s ease-out;
}}
.modal-title {{
    font-size: 20px;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 15px;
}}
.modal-text {{
    font-size: 16px;
    font-weight: bold;
    color: #166534;
    background-color: #f0fdf4;
    padding: 15px;
    border-radius: 14px;
    border: 1px solid #bbf7d0;
    margin-bottom: 20px;
    line-height: 1.6;
}}
.close-btn {{
    background-color: #ef4444;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 15px;
    font-weight: bold;
    border-radius: 12px;
    cursor: pointer;
    width: 100%;
    max-width: 200px;
    box-shadow: 0px 4px 12px rgba(239, 68, 68, 0.2);
}}
@keyframes popupAnim {{
    from {{ transform: scale(0.95); opacity: 0; }}
    to {{ transform: scale(1); opacity: 1; }}
}}
</style>
</head>
<body>
    <div class="tax-card">
        <div class="tax-card-title">
            🟢 محاسبه مالیات حقوق
        </div>
        <div class="tax-card-subtitle">مبلغ مزایای مشمول مالیات را پس از کسر معافیت‌ها (بیمه تامین اجتماعی و ...) وارد کنید</div>
        
        <div class="input-container">
            <div class="currency-label">ریال</div>
            <input type="text" id="salary" class="amount-input" placeholder="1,000,000,000" />
        </div>
        
        <div class="input-help-text">
            ℹ️ مبلغ را به ریال وارد کنید
        </div>

        <button class="calc-button" onclick="calculateTaxPopup()">
            ⚡ محاسبه مالیات
        </button>

        <div id="taxModal" class="modal-overlay">
            <div class="modal-box">
                <div class="modal-title">📊 نتیجه محاسبه مالیات حقوق</div>
                <div id="modalResult" class="modal-text"></div>
                <button class="close-btn" onclick="closeModal()">بستن پنجره</button>
            </div>
        </div>
    </div>

    <script>
    // جداکننده سه رقم سه رقم بدون خطا
    document.getElementById('salary').addEventListener('input',function (e) {{
        var value = e.target.value.replace(/,/g, '');
        if (value === "") {{
            e.target.value = "";
            return;
        }}
        e.target.value = parseInt(value).toLocaleString('en-US');
    }});

    function calculateTaxPopup() {{
        var val = document.getElementById('salary').value;
        var salaryNum = parseInt(val.replace(/,/g, '')) || 0;
        
        var tax = 0;
        var resultText = "";
        
        if (salaryNum <= 400000000) {{
            tax = 0;
        }} 
        else if (salaryNum <= 800000000) {{
            tax = (salaryNum - 400000000) * 0.10;
        }} 
        else if (salaryNum <= 1000000000) {{
            tax = (400000000 * 0.10) + (salaryNum - 800000000) * 0.15;
        }} 
        else if (salaryNum <= 1200000000) {{
            tax = (400000000 * 0.10) + (200000000 * 0.15) + (salaryNum - 1000000000) * 0.20;
        }} 
        else if (salaryNum <= 1400000000) {{
            tax = (400000000 * 0.10) + (200000000 * 0.15) + (200000000 * 0.20) + (salaryNum - 1200000000) * 0.25;
        }} 
        else {{
            tax = (400000000 * 0.10) + (200000000 * 0.15) + (200000000 * 0.20) + (200000000 * 0.25) + (salaryNum - 1400000000) * 0.30;
        }}

        if (tax === 0) {{
            resultText = "حقوق شما معاف از مالیات است. 🎉";
        }} else {{
            resultText = "💰 مالیات متعلق به حقوق شما: " + Math.floor(tax).toLocaleString() + " ریال";
        }}
        
        document.getElementById('modalResult').innerHTML = resultText;
        document.getElementById('taxModal').style.display = 'flex';
    }}

    function closeModal() {{
        document.getElementById('taxModal').style.display = 'none';
    }}
    </script>
</body>
</html>
""", height=350)