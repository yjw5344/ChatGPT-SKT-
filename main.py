from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
import torch
from pydantic import BaseModel, Field

tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token='</s>', eos_token='</s>', unk_token='<unk>',
    pad_token='<pad>', mask_token='<mask>')



model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

text = '근육이 커지기 위해서는 '
input_ids = tokenizer.encode(text)
gen_ids = model.generate(torch.tensor([input_ids]),
                         max_length=128,
                         repetition_penalty=2.0,
                         pad_token_id=tokenizer.pad_token_id,
                         eos_token_id=tokenizer.eos_token_id,
                         bos_token_id=tokenizer.bos_token_id,
                         use_cache=True)
generated = tokenizer.decode(gen_ids[0,:].tolist())
print(generated)