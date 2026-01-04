from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path
from typing import Dict

from dotenv import dotenv_values
from openai import OpenAI, OpenAIError

DEFAULT_SECRETS = Path(__file__).parent / "secrets" / "azure_openai.env"


def load_credentials(path: Path) -> Dict[str, str]:
    creds = {k: v for k, v in dotenv_values(path).items() if v} if path.exists() else {}
    for key in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY", "AZURE_OPENAI_DEPLOYMENT"):
        if not creds.get(key):
            env_value = os.getenv(key)
            if env_value:
                creds[key] = env_value
    missing = [k for k in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY", "AZURE_OPENAI_DEPLOYMENT") if not creds.get(k)]
    if missing:
        raise RuntimeError(f"Missing credentials: {', '.join(missing)}")
    return creds


def normalize_base_url(raw: str) -> str:
    cleaned = (raw or "").strip()
    if not cleaned:
        raise RuntimeError("AZURE_OPENAI_ENDPOINT must not be empty.")
    if not cleaned.endswith("/"):
        cleaned += "/"
    return cleaned


def run_smoke_test(*, base_url: str, deployment: str, api_key: str, prompt: str) -> dict:
    client = OpenAI(base_url=base_url, api_key=api_key)
    response = client.responses.create(
        model=deployment,
        input=prompt,
    )
    return response.model_dump()


def main() -> None:
    parser = argparse.ArgumentParser(description="Minimal Azure OpenAI endpoint smoke test.")
    parser.add_argument("--secrets-path", default=str(DEFAULT_SECRETS), help="Path to azure_openai.env")
    parser.add_argument("--prompt", default="What is the capital of France?", help="Prompt to send to the model")
    parser.add_argument(
        "--endpoint",
        default=None,
        help="Override the endpoint base URL (defaults to AZURE_OPENAI_ENDPOINT)",
    )
    parser.add_argument(
        "--deployment",
        default=None,
        help="Override deployment/model name (defaults to AZURE_OPENAI_DEPLOYMENT)",
    )
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="[%(levelname)s] %(message)s")

    creds = load_credentials(Path(args.secrets_path))
    base_url = normalize_base_url(args.endpoint or creds["AZURE_OPENAI_ENDPOINT"])
    deployment = args.deployment or creds["AZURE_OPENAI_DEPLOYMENT"]
    logging.info("Testing endpoint %s with deployment %s", base_url, deployment)
    try:
        payload = run_smoke_test(
            base_url=base_url,
            deployment=deployment,
            api_key=creds["AZURE_OPENAI_KEY"],
            prompt=args.prompt,
        )
    except OpenAIError as exc:
        logging.error("Request failed: %s", exc)
        raise SystemExit(1)

    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
