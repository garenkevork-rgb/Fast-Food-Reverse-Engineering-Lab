import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="  مختبر الهندسة العكسية للوجبات السريعة",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #f8fafc;
    --panel: #ffffff;
    --panel-light: #f1f5f9;
    --border: #cbd5e1;
    --text: #0f172a;
    --muted: #64748b;
    --accent: #10b981;
    --blue: #2563eb;
}

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-left: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--text);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* تنسيق الهيرو وجعل العناوين عريضة جداً واحترافية */
.hero {
    padding: 36px;
    border: 2px solid #94a3b8;
    border-radius: 24px;
    background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
    margin-bottom: 28px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
}

.hero-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 30px;
    background: #d1fae5;
    color: #047857;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero h1 {
    color: #0f172a;
    font-size: clamp(28px, 3vw, 42px);
    font-weight: 900;
    letter-spacing: -0.5px;
    margin: 0 0 8px 0;
}

.hero .food-subtitle {
    font-weight: 800;
    color: #059669;
    font-size: 18px;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

.hero p {
    color: #334155;
    font-size: 16px;
    font-weight: 600;
    line-height: 1.8;
    margin: 0;
}

.section-title {
    color: #0f172a;
    font-size: 24px;
    font-weight: 900;
    margin: 28px 0 16px;
    border-right: 5px solid #10b981;
    padding-right: 12px;
}

.ingredients-box {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    padding: 16px 20px;
    border-radius: 12px;
    margin-bottom: 16px;
    color: #1e293b;
    font-size: 15px;
    font-weight: 700;
}

.additions-box {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    padding: 16px 20px;
    border-radius: 12px;
    margin-bottom: 16px;
    color: #065f46;
    font-size: 15px;
    font-weight: 700;
}

div[data-testid="stMetric"] {
    background: var(--panel);
    border: 1px solid var(--border);
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    transition: transform .2s, border-color .2s;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
}

div[data-testid="stMetricLabel"] {
    color: var(--muted);
    font-weight: 700;
}

div[data-testid="stMetricValue"] {
    color: #0f172a;
    font-weight: 900;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #10b981, #059669);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    min-height: 50px;
    font-weight: 900;
    transition: transform .2s;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    border: none;
}

.stSelectbox > div > div,
.stNumberInput > div > div {
    background: var(--panel);
    border-color: var(--border);
    border-radius: 10px;
}

div[data-testid="stImage"] img {
    border-radius: 18px;
    border: 2px solid var(--border);
}

hr {
    border-color: var(--border);
    margin: 32px 0;
}

small, .muted {
    color: var(--muted);
    font-weight: 600;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }
    .hero {
        padding: 22px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# Hero section مع جعل العنوان بارز وعريض جداً
st.markdown(
    """
<div class="hero">
    <div class="hero-badge">🔬 منصة التحليل الغذائي المتقدمة</div>
    <h1>مختبر الهندسة العكسية للوجبات السريعة</h1>
    <div class="food-subtitle">🍔 Fast-Food Reverse-Engineering Lab Dashboard</div>
    <p>نظام ذكي متكامل لاستعراض وجبات المطاعم، محاكاة المكونات والإضافات بدقة رياضية، وحساب أوقات الحرق والقرار الهندسي النهائي.</p>
</div>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
  try:
    df_loaded = pd.read_csv("Fast_Food_Reverse_Engineering_Lab_Data.csv")
    return df_loaded
  except:
    np.random.seed(42)
    chains = [
        "McDonald's",
        "KFC",
        "Burger King",
        "Taco Bell",
        "Dominos's Pizza",
        "Wendy's",
    ]
    categories = [
        "Pizza Feast & Cheesy Bread",
        "Loaded Burrito, Nachos & Soda",
        "Late-Night Value Menu Binge",
        "Fried Chicken Bucket & Slaw",
        "Double Burger & Large Fry",
        "Dessert Overload & Large Shake",
    ]
    sample_ingredients = [
        "عجينة بيتزا سميكة، صلصة طماطم، جبنة موتسريلا مضاعفة، خبز بالثوم والجبن المحمص",
        "بورريتو محشو باللحم المفروم، فاصوليا، أرز مكسيكي، تورتيلا، ناتشوز مع صوص الجبنة ومشروب غازي",
        "وجبة ليلية دسمة تتضمن برجر مزدوج، بطاطس مقلية مقرمشة، صوصات غنية ومشروب منعش",
        "قطع دجاج مقرمش في سطل كبير، بهارات مقلية حارة، سلطة كولسلو منعشة، بطاطس مقلية",
        "قطعتي برجر لحم بقر، جبنة شيدر ذائبة، خبز بالسمسم، بطاطس مقلية كبيرة مقرمشة",
        "تشيز كيك فواكه، صوص شوكولاتة غامق، ميلك شيك فانيليا دسم وإضافات سكرية",
    ]
    data = {
        "order_id": [f"FFC-{i:05d}" for i in range(1, 31)],
        "fast_food_chain": np.random.choice(chains, 30),
        "meal_category": np.random.choice(categories, 30),
        "base_ingredients": np.random.choice(sample_ingredients, 30),
        "total_calories": np.random.uniform(600, 2200, 30),
        "fat_grams": np.random.uniform(20, 110, 30),
        "saturated_fat_grams": np.random.uniform(5, 45, 30),
        "carb_grams": np.random.uniform(40, 220, 30),
        "sugar_grams": np.random.uniform(5, 60, 30),
        "protein_grams": np.random.uniform(20, 80, 30),
        "sodium_mg": np.random.uniform(800, 3500, 30),
    }
    return pd.DataFrame(data)


df = load_data()


def get_meal_image(category):
  cat = str(category).lower()
  if "pizza" in cat or "bread" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_m3oyvwm3oyvwm3oy.jpg"
  elif "burrito" in cat or "nachos" in cat or "soda" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_24bqn024bqn024bq.jpg"
  elif "late-night" in cat or "binge" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_edncksedncksednc.jpg"
  elif "chicken" in cat or "bucket" in cat or "slaw" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_c8deokc8deokc8de.jpg"
  elif "double burger" in cat or "fry" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_6e0acw6e0acw6e0a.jpg"
  elif "dessert" in cat or "shake" in cat or "overload" in cat:
    return r"C:\Users\User\Downloads\Gemini_Generated_Image_91yy0l91yy0l91yy.jpg"
  else:
    return "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600"


def get_available_additions_text(category):
  cat = str(category).lower()
  if "dessert" in cat or "shake" in cat or "overload" in cat:
    return (
        "🍰 **المواد المتاحة للإضافة:** صوص شوكولاتة مركز، شربات سكري، آيس كريم"
        " إضافي، قطع تشيز كيك."
    )
  elif "pizza" in cat or "bread" in cat:
    return (
        "🍕 **المواد المتاحة للإضافة:** جبنة موتسريلا مضاعفة، صلصة طماطم إضافية،"
        " شرائح خبز بالثوم والجبن المحمص."
    )
  elif "burger" in cat or "fry" in cat:
    return (
        "🍔 **المواد المتاحة للإضافة:** شرائح جبن شيدر ذائبة، صوص خاص دسم، بطاطس"
        " مقلية إضافية، لحم بقر إضافي."
    )
  elif "burrito" in cat or "nachos" in cat or "soda" in cat:
    return (
        "🌯 **المواد المتاحة للإضافة:** صوص جبنة ناتشوز، أرز مكسيكي، لحم مفروم"
        " إضافي، فاصوليا."
    )
  elif "chicken" in cat or "bucket" in cat or "slaw" in cat:
    return (
        "🍗 **المواد المتاحة للإضافة:** قطع دجاج مقرمش إضافية، صوص حار، سلطة"
        " كولسلو غنية بالمايونيز، بطاطس."
    )
  else:
    return (
        "✨ **المواد المتاحة للإضافة:** صوصات مخصصة، جبنة إضافية، مكونات كبرى"
        " (دهون/كارب/بروتين)."
    )


st.markdown(
    '<div class="section-title">🔬 محطة اختيار الوجبات</div>',
    unsafe_allow_html=True,
)

col_sel1, col_sel2 = st.columns(2)
with col_sel1:
  selected_chain = st.selectbox(
      "🏢 اختر سلسلة المطاعم:", df["fast_food_chain"].unique()
  )

with col_sel2:
  selected_meal_category = st.selectbox(
      "🍔 اختر اسم الوجبة:", df["meal_category"].unique()
  )

meal_filtered = df[
    (df["fast_food_chain"] == selected_chain)
    & (df["meal_category"] == selected_meal_category)
]
if meal_filtered.empty:
  meal_row = df[df["meal_category"] == selected_meal_category].iloc[0]
else:
  meal_row = meal_filtered.iloc[0]

st.markdown("<hr>", unsafe_allow_html=True)

img_col, details_col = st.columns([1, 2])

with img_col:
  img_url = get_meal_image(meal_row["meal_category"])
  st.image(
      img_url, caption=f"وجبة: {meal_row['meal_category']}", use_container_width=True
  )

with details_col:
  st.markdown(
      f'<div class="section-title" style="margin-top:0;">📋 المكونات الأساسية'
      f" لـ {selected_chain} - {meal_row['meal_category']}</div>",
      unsafe_allow_html=True,
  )

  ingredients_text = meal_row.get(
      "base_ingredients",
      "مكونات وجبة أساسية (برجر، جبنة، صوص، بطاطس أو حلويات)",
  )
  st.markdown(
      f'<div class="ingredients-box">📝 <b>مكونات الوجبة:</b>'
      f" {ingredients_text}</div>",
      unsafe_allow_html=True,
  )

  additions_guide = get_available_additions_text(meal_row["meal_category"])
  st.markdown(
      f'<div class="additions-box">{additions_guide}</div>',
      unsafe_allow_html=True,
  )

  b1, b2, b3 = st.columns(3)
  b1.metric("🔥 السعرات الأساسية", f"{meal_row['total_calories']:.1f} kcal")
  b2.metric("🥩 البروتين", f"{meal_row['protein_grams']:.1f} g")
  b3.metric("🥔 الكربوهيدرات", f"{meal_row['carb_grams']:.1f} g")

  s1, s2, s3, s4 = st.columns(4)
  s1.metric("🧈 الدهون الكلية", f"{meal_row['fat_grams']:.1f} g")
  s2.metric("🧂 الصوديوم", f"{meal_row['sodium_mg']:.1f} mg")
  s3.metric("🍬 السكريات", f"{meal_row.get('sugar_grams', 20):.1f} g")
  s4.metric("⚠️ الدهون المشبعة", f"{meal_row['saturated_fat_grams']:.1f} g")

st.markdown("<hr>", unsafe_allow_html=True)

if "reset_trigger" not in st.session_state:
  st.session_state.reset_trigger = 0

if st.button("🔄 إعادة ضبط الوجبة (كما يقدمها المطعم)"):
  st.session_state.reset_trigger += 1
  st.rerun()

st.markdown(
    '<div class="section-title">⚖️ مقارنة ومحاكاة التعديل الذكي (الوجبة الأصلية'
    ' مقابل تخصيص الزبون)</div>',
    unsafe_allow_html=True,
)

col_right_restaurant, col_left_customer = st.columns(2)

# --- العمود الأيمن: وجبة المطعم الأصلية ---
with col_right_restaurant:
  st.markdown("### 🏢 وجبة المطعم الأصلية (بدون تعديل)")
  st.markdown(
      '<p class="muted">القيم الأساسية كما تأتي من المطبخ:</p>',
      unsafe_allow_html=True,
  )

  orig_calories = meal_row["total_calories"]
  orig_protein = meal_row["protein_grams"]
  orig_carb = meal_row["carb_grams"]
  orig_fat = meal_row["fat_grams"]
  orig_sodium = meal_row["sodium_mg"]
  orig_sat = meal_row["saturated_fat_grams"]

  # الاعتماد على المعادلات الجديدة بدقة
  orig_walk = max(0, (0.2186 * orig_calories) + (-4.6208 * 70) + 359.38)
  orig_run = max(0, (0.0736 * orig_calories) + (-1.5541 * 70) + 120.81)
  orig_hiit = max(0, (0.0627 * orig_calories) + (-1.3195 * 70) + 102.68)

  st.metric("🔥 السعرات الأصلية", f"{orig_calories:.1f} kcal")
  st.metric("🥩 البروتين", f"{orig_protein:.1f} g")
  st.metric("🥔 الكربوهيدرات", f"{orig_carb:.1f} g")
  st.metric("🧈 الدهون الكلية", f"{orig_fat:.1f} g")
  st.metric("🧂 الصوديوم", f"{orig_sodium:.1f} mg")

  st.markdown("---")
  st.markdown("🏃‍♂️ **أوقات الحرق الأصلية (وزن 70 كغ):**")
  st.info(
      f"🚶‍♂️ مشي: {orig_walk:.1f} دقيقة | 🏃‍♂️ جري: {orig_run:.1f} دقيقة | 🔥"
      f" HIIT: {orig_hiit:.1f} دقيقة"
  )

# --- العمود الأيسر: تخصيص الزبون والداشبورد ---
with col_left_customer:
  st.markdown("### 🛠️ تخصيص الزبون (أريد أن أعدل / أضيف)")
  st.markdown(
      '<p class="muted">تحكم بالإضافات ووزن المستهلك لمشاهدة تأثيرها'
      " لحظياً:</p>",
      unsafe_allow_html=True,
  )

  added_fat = st.slider(
      "إضافة دهون / صوصات دسمة (g)",
      0.0,
      40.0,
      0.0,
      1.0,
      key=f"fat_{st.session_state.reset_trigger}",
  )

  is_dessert = (
      "dessert" in str(meal_row["meal_category"]).lower()
      or "shake" in str(meal_row["meal_category"]).lower()
      or "overload" in str(meal_row["meal_category"]).lower()
  )
  carb_slider_label = (
      "إضافة كربوهيدرات / سكريات وشراب (g)"
      if is_dessert
      else "إضافة كربوهيدرات / خبز أو بطاطس (g)"
  )

  added_carb = st.slider(
      carb_slider_label,
      0.0,
      50.0,
      0.0,
      1.0,
      key=f"carb_{st.session_state.reset_trigger}",
  )
  added_protein = st.slider(
      "إضافة بروتين (g)",
      0.0,
      30.0,
      0.0,
      1.0,
      key=f"pro_{st.session_state.reset_trigger}",
  )

  consumer_weight = st.slider(
      "وزن المستهلك للتمارين (kg):",
      50.0,
      120.0,
      70.0,
      1.0,
      key=f"weight_{st.session_state.reset_trigger}",
  )

  new_fat = orig_fat + added_fat
  new_carb = orig_carb + added_carb
  new_protein = orig_protein + added_protein

  # تطبيق المعادلات الجديدة الدقيقة المعتمدة
  new_calories = (
      (9.08 * new_fat) + (4.03 * new_carb) + (4.17 * new_protein) - 19.47
  )
  new_sodium = (
      (1.389 * new_fat)
      + (5.83 * new_carb)
      + (6.12 * new_protein)
      + (-11.55)
      + (1.4131 * new_calories)
      / 10  # معادلة الصوديوم المستخرجة بدقة
  )
  new_tef = (0.0738 * new_calories) + 3.34
  new_sat_fat = (0.3949 * new_fat) + 0.37

  walk_time = max(
      0, (0.2186 * new_calories) + (-4.6208 * consumer_weight) + 359.38
  )
  run_time = max(
      0, (0.0736 * new_calories) + (-1.5541 * consumer_weight) + 120.81
  )
  hiit_time = max(
      0, (0.0627 * new_calories) + (-1.3195 * consumer_weight) + 102.68
  )

  st.markdown("---")
  st.markdown("📊 **داشبورد النتائج الجديدة بعد التعديل:**")

  rc1, rc2 = st.columns(2)
  rc1.metric(
      "🔥 السعرات الجديدة",
      f"{new_calories:.1f} kcal",
      delta=f"{new_calories - orig_calories:+.1f}",
  )
  rc2.metric(
      "🧂 الصوديوم الجديد",
      f"{new_sodium:.1f} mg",
      delta=f"{new_sodium - orig_sodium:+.1f}",
  )

  rc3, rc4 = st.columns(2)
  rc3.metric("⚡ التأثير الحراري TEF", f"{new_tef:.1f} kcal")
  rc4.metric(
      "⚠️ الدهون المشبعة",
      f"{new_sat_fat:.1f} g",
      delta=f"{new_sat_fat - orig_sat:+.1f}",
  )

  st.markdown("🏃‍♂️ **أوقات الحرق الجديدة (حسب وزنك):**")
  st.success(
      f"🚶‍♂️ مشي: {walk_time:.1f} دقيقة | 🏃‍♂️ جري: {run_time:.1f} دقيقة | 🔥"
      f" HIIT: {hiit_time:.1f} دقيقة"
  )

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="section-title">📐 التوثيق الرياضي: المعادلات المستخدمة في'
    " المحرك</div>",
    unsafe_allow_html=True,
)
st.markdown("""
تم اعتماد المعادلات النهائية والدقيقة المستخرجة في مختبر الهندسة العكسية:

- **1. معادلة السعرات الكلية ($R^2 = 0.9990$):**  
  $$\\text{Total Calories} = (9.08 \\times \\text{Fat}) + (4.03 \\times \\text{Carb}) + (4.17 \\times \\text{Protein}) - 19.47$$

- **2. معادلة الصوديوم ($R^2 = 0.8667$):**  
  $$\\text{Sodium} = (1.389 \\times \\text{Fat}) + (5.83 \\times \\text{Carb}) + (6.12 \\times \\text{Protein}) - 11.55$$

- **3. معادلة زمن حرق المشي ($R^2 = 0.9432$):**  
  $$\\text{Walking Burn Time} = (0.2186 \\times \\text{Total Calories}) + (-4.6208 \\times \\text{Consumer Weight}) + 359.38$$

- **4. معادلة التأثير الحراري للطعام ($R^2 = 0.8845$):**  
  $$\\text{Thermic Effect} = (0.0738 \\times \\text{Total Calories}) + 3.34$$

- **5. معادلة الدهون المشبعة ($R^2 = 0.8841$):**  
  $$\\text{Saturated Fat} = (0.3949 \\times \\text{Fat}) + 0.37$$

- **6. معادلة زمن حرق الجري ($R^2 = 0.9400$):**  
  $$\\text{Running Burn Time} = (0.0736 \\times \\text{Total Calories}) + (-1.5541 \\times \\text{Consumer Weight}) + 120.81$$

- **7. معادلة زمن حرق HIIT ($R^2 = 0.9381$):**  
  $$\\text{HIIT Burn Time} = (0.0627 \\times \\text{Total Calories}) + (-1.3195 \\times \\text{Consumer Weight}) + 102.68$$
""")