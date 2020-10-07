from easydict import EasyDict as edict
import mindspore.common.dtype as mstype
from .GPT2_model import GPT2Config

cfg = edict({
    'gpt2_network': 'small',
    'optimizer': 'Lamb',
    'AdamWeightDecay': edict({
        'learning_rate': 2e-5,
        'end_learning_rate': 1e-7,
        'power': 1.0,
        'weight_decay': 1e-5,
        'decay_filter': lambda x: 'layernorm' not in x.name.lower() and 'bias' not in x.name.lower(),
        'eps': 1e-6,
    }),
    'Lamb': edict({
        'learning_rate': 2e-5,
        'end_learning_rate': 1e-7,
        'power': 1.0,
        'weight_decay': 0.01,
        'decay_filter': lambda x: 'layernorm' not in x.name.lower() and 'bias' not in x.name.lower(),
    }),
    'Momentum': edict({
        'learning_rate': 2e-5,
        'momentum': 0.9,
    }),
})

"""
three kinds of GPT2 model version
"""
if cfg.gpt2_network == 'small':
    gpt2_net_cfg = GPT2Config(
        batch_size=512,
        seq_length=1024,
        vocab_size=50257,
        d_model=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout=0.1,
        attention_dropout=0.1,
        max_position_embeddings=1024,
        initializer_range=0.02,
        input_mask_from_dataset=True,
        dtype=mstype.float32,
        compute_type=mstype.float32,
    )
if cfg.gpt2_network == 'medium':
    gpt2_net_cfg = GPT2Config(
        batch_size=512,
        seq_length=1024,
        vocab_size=50257,
        d_model=1024,
        num_hidden_layers=24,
        num_attention_heads=16,
        intermediate_size=4096,
        hidden_act="gelu",
        hidden_dropout=0.1,
        attention_dropout=0.1,
        max_position_embeddings=1024,
        initializer_range=0.02,
        input_mask_from_dataset=True,
        dtype=mstype.float32,
        compute_type=mstype.float32,
    )
if cfg.gpt2_network == 'large':
    gpt2_net_cfg = GPT2Config(
        batch_size=512,
        seq_length=1024,
        vocab_size=50257,
        d_model=1280,
        num_hidden_layers=36,
        num_attention_heads=20,
        intermediate_size=5120,
        hidden_act="gelu",
        hidden_dropout=0.1,
        attention_dropout=0.1,
        max_position_embeddings=1024,
        initializer_range=0.02,
        input_mask_from_dataset=True,
        dtype=mstype.float32,
        compute_type=mstype.float32,
    )