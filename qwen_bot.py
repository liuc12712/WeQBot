from transformers import AutoModelForCausalLM, AutoTokenizer

import time

model_path = "models/qwen2.5_3B"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="cuda"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 初始化对话历史
conversation_history = [
    {"role": "system",
     "content": "你的名字是 WeQBot，你是由 Github 个人用户 'LiuceCN' 结合 Qwen 2.5-3B 模型和 wxauto 库开发的专门为微信自动化回复的程序，你是个有用的助手。尽可能多发emojis表情。"}
]


def qwen2_5(ask):
    start_time = time.time()
    # 将用户输入添加到对话历史中
    conversation_history.append({"role": "user", "content": ask})

    # 使用对话历史生成模型输入
    text = tokenizer.apply_chat_template(
        conversation_history,
        tokenize=False,
        add_generation_prompt=True
    )

    # 转换成模型需要的输入格式
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # 生成回答
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )

    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    # 解码生成的结果
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # 将模型的回答添加到对话历史中，以便下次生成时参考
    conversation_history.append({"role": "assistant", "content": response})

    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算耗时
    # print(f"模型处理时间: {elapsed_time:.4f}秒")

    return response,elapsed_time
