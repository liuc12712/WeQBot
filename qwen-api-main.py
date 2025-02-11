from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

# 创建 Flask 应用
app = Flask(__name__)

device = "cuda" # the device to load the model onto
# 加载分词器和模型
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-1.8B-Chat",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-1.8B-Chat")

def qwen(issue):
    prompt = issue
    messages = [
        {"role": "system", "content": "Your name is WeQBot and it was developed by Liuce CN in combination with the Qwen 1.5 model and the wxauto library，You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response

@app.route('/process', methods=['POST'])
def process():
    # 从请求体中获取数据
    data = request.json
    if not data or 'a' not in data:
        return jsonify({"error": "Missing 'a' in request"}), 400

    # 获取变量 a
    a = data['a']

    # 调用自定义函数处理数据
    b = qwen(a)

    # 返回处理结果
    return jsonify({"b": b})

# 启动服务
if __name__ == '__main__':
    app.run(port=5000)
