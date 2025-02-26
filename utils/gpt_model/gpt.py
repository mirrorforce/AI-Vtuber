# -*- coding: UTF-8 -*-
"""
@Project : AI-Vtuber 
@File    : gpt.py
@Author  : HildaM
@Email   : Hilda_quan@163.com
@Date    : 2023/06/23 下午 7:47 
@Description :  统一模型层抽象
"""
import logging

from utils.gpt_model.chatglm import Chatglm
from utils.gpt_model.chatgpt import Chatgpt
from utils.gpt_model.claude import Claude
from utils.gpt_model.text_generation_webui import TEXT_GENERATION_WEBUI
from utils.gpt_model.sparkdesk import SPARKDESK


class GPT_Model:
    # 模型配置信息
    openai = None  # 只有openai是config配置，其他均是实例
    chatgpt = None
    claude = None
    chatglm = None
    text_generation_webui = None
    sparkdesk = None

    def set_model_config(self, model_name, config):
        if model_name == "openai":
            self.openai = config
        elif model_name == "chatgpt":
            if self.openai is None:
                logging.error("openai key 为空，无法配置chatgpt模型")
                exit(-1)
            self.chatgpt = Chatgpt(self.openai, config)
        elif model_name == "claude":
            self.claude = Claude(config)
        elif model_name == "chatglm":
            self.chatglm = Chatglm(config)
        elif model_name == "text_generation_webui":
            self.text_generation_webui = TEXT_GENERATION_WEBUI(config)
        elif model_name == "sparkdesk":
            self.sparkdesk = SPARKDESK(config)

    def get(self, name):
        logging.info("GPT_MODEL: 进入get方法")
        match name:
            case "openai":
                return self.openai
            case "chatgpt":
                return self.chatgpt
            case "claude":
                return self.claude
            case "chatglm":
                return self.chatglm
            case "text_generation_webui":
                return self.text_generation_webui
            case "sparkdesk":
                return self.sparkdesk
            case _:
                logging.error(f"{name} 该模型不支持")
                return

    def get_openai_key(self):
        if self.openai is None:
            logging.error("openai_key 为空")
            return None
        return self.openai["api_key"]

    def get_openai_model_name(self):
        if self.openai is None:
            logging.warning("openai的model为空，将设置为默认gpt-3.5")
            return "gpt-3.5-turbo-0301"
        return self.openai["model"]


# 全局变量
GPT_MODEL = GPT_Model()
