from utils import run_llama

def sales_pitch(product):
    prompt = f"Create a persuasive sales pitch for this product/service:\n{product}"
    return run_llama(prompt)

if __name__ == "__main__":
    product = input("Describe your product: ")
    print(sales_pitch(product))
