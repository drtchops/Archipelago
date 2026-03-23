import asyncio
from argparse import Namespace
from typing import Any

from CommonClient import CommonContext, get_base_parser, server_loop
from Utils import gui_enabled


class ProxyCommandProcessor(CommonContext.command_processor):
    pass


def run(*launcher_args: Any) -> None:
    class ProxyContext(CommonContext):
        tags = CommonContext.tags | {"TextOnly"}
        game = ""
        command_processor = ProxyCommandProcessor

        async def server_auth(self, password_requested: bool = False) -> None:
            if password_requested and not self.password:
                await super().server_auth(password_requested)
            await self.get_username()
            await self.send_connect(game="")

        def on_package(self, cmd: str, args: dict) -> None:
            super().on_package(cmd, args)
            if cmd == "Connected":
                self.game = self.slot_info[self.slot].game

        async def disconnect(self, allow_autoreconnect: bool = False) -> None:
            self.game = ""
            await super().disconnect(allow_autoreconnect)

    async def main(args: Namespace) -> None:
        ctx = ProxyContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Proxy Archipelago Client, for getting compression on outdated clients.")
    parsed_args = parser.parse_args(launcher_args)
    colorama.just_fix_windows_console()
    asyncio.run(main(parsed_args))
    colorama.deinit()
