import os

print("🚀 开始运行 GitHub Actions 测试...")

# 尝试读取你在 GitHub Secrets 里配置的 MOONSHOT_API_KEY
api_key = os.getenv("MOONSHOT_API_KEY")

if api_key:
    print(f"✅ 成功！Secrets 注入正常。")
    print(f"🔑 API Key 前5位是: {api_key[:5]}... (为了安全不显示全部)")
else:
    print("❌ 失败！没找到 MOONSHOT_API_KEY。")
    print("💡 请检查：Settings -> Secrets -> Actions 里是否添加了这个名字的变量。")

print("🏁 脚本运行结束。")