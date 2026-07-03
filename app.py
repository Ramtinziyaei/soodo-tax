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
# ۲. بخش هدر سایت (Navbar)
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
    direction: ltr;
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
}}

.instagram-btn {{
    background: linear-gradient(135deg, #f9ce34 0%, #ee2a7b 50%, #6228d7 100%);
    color: white !important;
    padding: 10px 24px !important;
    border-radius: 50px;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0px 4px 15px rgba(238, 42, 123, 0.2);
    display: flex;
    align-items: center;
    gap: 8px;
}}

@media (max-width: 768px) {{
    .navbar {{
        padding: 10px 15px;
        flex-direction: column;
        height: auto;
        gap: 10px;
    }}
    .brand img {{ width: 70px; }}
    .brand-title {{ font-size: 20px; }}
    .menu {{ gap: 15px; width: 100%; justify-content: center; }}
    .menu a {{ font-size: 15px; }}
    .instagram-btn {{ padding: 6px 14px !important; font-size: 13px !important; }}
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
            <a href="https://instagram.com/soodoacademy" class="instagram-btn" target="_blank">📸 اینستاگرام ما</a>
        </div>
    </div>
</body>
</html>
""", height=110)

# =========================================================
# ۳. بخش معرفی (Hero Section) - تقسیم سهم مساوی (۳۳٪)
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
    justify-content: space-between;
    padding: 10px 5%;
    gap: 20px;
    width: 100%;
}}

/* تقسیم فضا به ۳ قسمت دقیقاً مساوی */
.hero-item {{
    flex: 1;
    width: 33.33%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.hero-right {{
    align-items: center;
}}

.hero-right img {{
    width: 100%;
    max-width: 280px;
    height: auto;
}}

.hero-center {{
    text-align: center;
    align-items: center;
    gap: 8px;
}}

.hero-title {{
    font-size: 26px;
    font-weight: 900;
    color: #1e293b;
    line-height: 1.4;
    margin: 0;
}}

.hero-title span {{
    color: #0f8f45;
}}

.hero-subtitle {{
    font-size: 14px;
    color: #64748b;
    line-height: 1.6;
    margin: 0;
}}

.features-container {{
    display: flex;
    gap: 6px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 5px;
}}

.feature-box {{
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 5px 10px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
    color: #334155;
    white-space: nowrap;
}}

.hero-left {{
    align-items: flex-start;
}}

.hero-info-card {{
    width: 100%;
    max-width: 340px;
    background-color: #f4fbf7;
    border: 1px dashed #0f8f45;
    border-radius: 16px;
    padding: 15px;
    text-align: right;
}}

.info-card-title {{
    font-size: 14px;
    font-weight: 800;
    color: #0f8f45;
    margin-bottom: 6px;
}}

.info-card-text {{
    font-size: 12.5px;
    color: #475569;
    line-height: 1.6;
}}

@media (max-width: 992px) {{
    .hero-section {{
        flex-direction: column;
        padding: 15px;
        gap: 20px;
    }}
    .hero-item {{
        width: 100%;
        text-align: center;
        align-items: center;
    }}
    .hero-left {{
        align-items: center;
    }}
    .hero-right img {{
        max-width: 200px;
    }}
}}
</style>
</head>
<body>
    <div class="hero-section">
        <!-- سمت راست: تصویر هیرو -->
        <div class="hero-item hero-right">
            {"<img src='data:image/png;base64," + calc_base64 + "'>" if calc_base64 else ""}
        </div>

        <!-- وسط: متن‌ها -->
        <div class="hero-item hero-center">
            <h1 class="hero-title">محاسبه‌گر سریع و تخمینی<br><span>مالیات حقوق</span></h1>
            <p class="hero-subtitle">برآورد مالیات حقوق بر اساس قوانین جاری، قبل از ارسال لیست حقوق</p>
            <div class="features-container">
                <div class="feature-box">🛡️ رایگان و امن</div>
                <div class="feature-box">⚡ محاسبه لحظه‌ای</div>
                <div class="feature-box">✅ سریع و دقیق</div>
            </div>
        </div>

        <!-- سمت چپ: کادر راهنما -->
        <div class="hero-item hero-left">
            <div class="hero-info-card">
                <div class="info-card-title">💡 این ابزار چیست؟</div>
                <div class="info-card-text">
                    این ابزار برای برآورد سریع مالیات حقوق بر اساس جدول مالیاتی سال جاری طراحی شده است. نتیجه نهایی پس از ارسال لیست در سامانه سازمان امور مالیاتی محاسبه و اعلام می‌شود.
                </div>
            </div>
        </div>
    </div>
</body>
</html>
""", height=250) # کاهش ارتفاع کامپوننت برای بالا آمدن کادر محاسبات

# =========================================================
# ۵. بخش فرم محاسبات - انتقال به بالاتر با کاهش پدینگ و مارجین
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
    padding: 20px 15px;
    margin: 0 auto; /* حذف مارجین بالا برای چسبیدن به بخش هیرو */
    width: 95%;
    max-width: 650px;
    text-align: center;
    position: relative;
}}
.tax-card-title {{
    font-size: 20px;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}}
.tax-card-subtitle {{
    font-size: 13px;
    color: #64748b;
    margin-bottom: 15px;
    padding: 0 5px;
    line-height: 1.6;
}}
.input-container {{
    display: flex;
    align-items: center;
    border: 2px solid #0f8f45;
    border-radius: 16px;
    overflow: hidden;
    width: 100%;
    margin: 0 auto 8px auto;
    background-color: white;
}}
.currency-label {{
    background-color: #f8fafc;
    border-right: 1px solid #e2e8f0;
    padding: 12px 18px;
    font-size: 15px;
    font-weight: bold;
    color: #1e293b;
}}
.amount-input {{
    flex: 1;
    border: none;
    padding: 12px 10px;
    font-size: 18px;
    font-weight: 700;
    color: #334155;
    text-align: center;
    outline: none;
    width: 100%;
}}
.input-help-text {{
    font-size: 12px;
    color: #64748b;
    margin-bottom: 12px;
}}
.calc-button {{
    background: linear-gradient(180deg, #0f8f45 0%, #0a6b33 100%);
    color: white;
    font-size: 17px;
    font-weight: 800;
    border: none;
    border-radius: 16px;
    padding: 14px 0;
    width: 100%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
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
    padding: 15px;
}}
.modal-box {{
    max-width: 450px;
    width: 100%;
    animation: popupAnim 0.25s ease-out;
}}
.modal-title {{
    font-size: 18px;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 12px;
}}
.modal-text {{
    font-size: 15px;
    font-weight: bold;
    color: #166534;
    background-color: #f0fdf4;
    padding: 12px;
    border-radius: 14px;
    border: 1px solid #bbf7d0;
    margin-bottom: 15px;
    line-height: 1.6;
}}
.close-btn {{
    background-color: #ef4444;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    border-radius: 12px;
    cursor: pointer;
    width: 100%;
    max-width: 160px;
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
        <div class="tax-card-title">🟢 محاسبه مالیات حقوق</div>
        <div class="tax-card-subtitle">مبلغ مزایای مشمول مالیات را پس از کسر معافیت‌ها (بیمه تامین اجتماعی و ...) وارد کنید</div>
        
        <div class="input-container">
            <div class="currency-label">ریال</div>
            <input type="text" id="salary" class="amount-input" placeholder="1,000,000,000" />
        </div>
        
        <div class="input-help-text">ℹ️ مبلغ را به ریال وارد کنید</div>

        <button class="calc-button" onclick="calculateTaxPopup()">
            ⚡ محاسبه مالیات
        </button>

        <div id="taxModal" class="modal-overlay">
            <div class="modal-box">
                <div class="modal-title">📊 نتیجه محاسبه مالیات حقوق</div>
                <div id="modalResult" class="modal-text"></div>
                <button class="close-btn" onclick="closeModal()">بستن پنجره</button>
            </div>
        </div></div>

    <script>
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
""", height=380)
