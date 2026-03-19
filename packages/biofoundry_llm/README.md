# Biofoundry LLM

Biofoundry LLM is an LLM abstraction layer designed for modern AI agent applications. It unifies message structures, asynchronous tool orchestration, and pluggable chat providers so you can build agents with ease and avoid vendor lock-in.

## Installation

Biofoundry LLM requires Python 3.12 or higher. We recommend using uv as the package manager.

Init your project with:

```bash
uv init --python 3.12  # or higher
```

Then add Biofoundry LLM as a dependency:

```bash
uv add biofoundry_llm
```

To enable optional providers such as Anthropic and Google Gemini, install the optional extra:

```bash
uv add 'biofoundry_llm[contrib]'
```

## Examples

### Simple chat completion

```python
import asyncio

import biofoundry_llm
from biofoundry_llm.contrib.chat_provider.openai_responses import OpenAIResponses
from biofoundry_llm.message import Message


async def main() -> None:
    openai = OpenAIResponses(
        base_url="https://api.openai.com/v1",
        api_key="your_openai_api_key_here",
        model="gpt-5",
    )

    history = [
        Message(role="user", content="Who are you?"),
    ]

    result = await biofoundry_llm.generate(
        chat_provider=openai,
        system_prompt="You are a helpful assistant.",
        tools=[],
        history=history,
    )
    print(result.message)
    print(result.usage)


asyncio.run(main())
```

### Streaming output

```python
import asyncio

import biofoundry_llm
from biofoundry_llm.chat_provider import StreamedMessagePart
from biofoundry_llm.contrib.chat_provider.openai_responses import OpenAIResponses
from biofoundry_llm.message import Message


async def main() -> None:
    openai = OpenAIResponses(
        base_url="https://api.openai.com/v1",
        api_key="your_openai_api_key_here",
        model="gpt-5",
    )

    history = [
        Message(role="user", content="Who are you?"),
    ]

    def output(message_part: StreamedMessagePart):
        print(message_part)

    result = await biofoundry_llm.generate(
        chat_provider=openai,
        system_prompt="You are a helpful assistant.",
        tools=[],
        history=history,
        on_message_part=output,
    )
    print(result.message)
    print(result.usage)


asyncio.run(main())
```

### Tool calling with `biofoundry_llm.step`

```python
import asyncio

from pydantic import BaseModel

import biofoundry_llm
from biofoundry_llm import StepResult
from biofoundry_llm.contrib.chat_provider.openai_responses import OpenAIResponses
from biofoundry_llm.message import Message
from biofoundry_llm.tooling import CallableTool2, ToolOk, ToolReturnValue
from biofoundry_llm.tooling.simple import SimpleToolset


class AddToolParams(BaseModel):
    a: int
    b: int


class AddTool(CallableTool2[AddToolParams]):
    name: str = "add"
    description: str = "Add two integers."
    params: type[AddToolParams] = AddToolParams

    async def __call__(self, params: AddToolParams) -> ToolReturnValue:
        return ToolOk(output=str(params.a + params.b))


async def main() -> None:
    openai = OpenAIResponses(
        base_url="https://api.openai.com/v1",
        api_key="your_openai_api_key_here",
        model="gpt-5",
    )

    toolset = SimpleToolset()
    toolset += AddTool()

    history = [
        Message(role="user", content="Please add 2 and 3 with the add tool."),
    ]

    result: StepResult = await biofoundry_llm.step(
        chat_provider=openai,
        system_prompt="You are a precise math tutor.",
        toolset=toolset,
        history=history,
    )
    print(result.message)
    print(await result.tool_results())


asyncio.run(main())
```

## Builtin Demo

Biofoundry LLM comes with a builtin demo agent that you can run locally. To start the demo, run:

```sh
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_KEY="your_openai_api_key"

uv run python -m biofoundry_llm openai --with-bash
```

## Development

To set up a development environment, clone the repository and install the dependencies:

```bash
# clone the repository you are working in
uv sync --all-extras

make check  # run lint and type checks
make test   # run tests
make format # format code
```
