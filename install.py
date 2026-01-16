import subprocess
import sys

# 分批安装，避免冲突
batches = [
    # 第一批：基础包
    ["pip", "install", "setuptools>=68.0", "wheel>=0.40"],

    # 第二批：核心异步包
    ["pip", "install", "aiofiles==23.2.1", "aiohttp==3.9.1", "aiosignal==1.3.1"],

    # 第三批：数据科学基础
    ["pip", "install", "numpy==1.26.2", "pandas==2.1.3"],

    # 第四批：LangChain 核心
    ["pip", "install", "langchain-core==0.1.26", "langchain==0.1.9", "openai==1.12.0"],

    # 第五批：剩余包
    ["pip", "install", "-r", "requirements.txt"]
]


def install_packages():
    print("开始安装依赖包...")

    for i, cmd in enumerate(batches, 1):
        print(f"\n{'=' * 50}")
        print(f"正在安装第 {i}/{len(batches)} 批包...")
        print(f"命令: {' '.join(cmd)}")
        print('=' * 50)

        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("✓ 安装成功")
            if result.stdout:
                print("输出:", result.stdout[-500:])  # 显示最后500字符
        except subprocess.CalledProcessError as e:
            print("✗ 安装失败")
            print("错误信息:", e.stderr)
            print("继续尝试安装下一批...")
            continue

    print("\n安装完成！")


if __name__ == "__main__":
    install_packages()