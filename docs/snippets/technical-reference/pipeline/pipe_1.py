import os

from distilabel.llm import InferenceEndpointsLLM
from distilabel.pipeline import pipeline
from distilabel.tasks import TextGenerationTask

pipe = pipeline(
    "preference",
    "text-quality",
    generator=InferenceEndpointsLLM(
        endpoint_name=endpoint_name,  # noqa: F821
        endpoint_namespace=endpoint_namespace,  # noqa: F821
        token=token,  # noqa: F821
        task=TextGenerationTask(),
        max_new_tokens=512,
        do_sample=True,
        prompt_format="notus",
    ),
    max_new_tokens=256,
    num_threads=2,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.0,
)
