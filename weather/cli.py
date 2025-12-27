import argparse
from importlib.metadata import PackageNotFoundError, metadata

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from weather.api import fetch_current, fetch_forecast

console = Console()


def show_about():
    try:
        meta = metadata("weather_cli")
    except PackageNotFoundError:
        console.print("[red]Package metadata not found[/]")
        return

    ASCII_LOGO = r"""
 Y8b Y8b Y888P                   d8   888                          e88'Y88 888     888
 Y8b Y8b Y8P   ,e e,   ,"Y88b  d88   888 ee   ,e e,  888,8,      d888  'Y 888     888
  Y8b Y8b Y   d88 88b "8" 888 d88888 888 88b d88 88b 888 "  888 C8888     888     888
   Y8b Y8b    888   , ,ee 888  888   888 888 888   , 888         Y888  ,d 888  ,d 888
    Y8P Y      "YeeP" "88 888  888   888 888  "YeeP" 888          "88,d88 888,d88 888
"""

    console.print(f"[magenta]{ASCII_LOGO}[/magenta]")

    body = f"""
[bold cyan]Author:[/] {meta.get("Author", "Unknown")}
[bold cyan]Version:[/] {meta.get("Version", "Unknown")}
[bold cyan]License:[/] {meta.get("License", "Unknown")}

[dim]{meta.get("Summary", "")}[/dim]

"""

    console.print(Panel(body, border_style="blue"))


def show_current(data):
    panel = Panel(
        f"""
🌡️ [magenta]Temp: [bold cyan]{data['main']['temp']}°[/]
🤗 [magenta]Feels: [cyan]{data['main']['feels_like']}°[/]
💧 [magenta]Humidity: [cyan]{data['main']['humidity']}%[/]
☁️ {data['weather'][0]['description'].capitalize()}
""",
        title=f"[yellow]Weather in {data['name']}",
        border_style="blue",
    )

    console.print(panel)


def show_forecast(data):
    table = Table(
        title="[yellow]5-Day Forecast",
        border_style="blue",
        header_style="bold magenta",
        expand=True,
    )
    table.add_column("Date", style="cyan")
    table.add_column("Temp (°)", style="cyan")
    table.add_column("Condition", style="cyan")

    seen = set()
    for entry in data["list"]:
        date = entry["dt_txt"].split(" ")[0]
        if date in seen:
            continue
        seen.add(date)

        table.add_row(
            date,
            f"{entry['main']['temp']}°",
            entry["weather"][0]["description"].capitalize(),
        )

        if len(seen) == 5:
            break

    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="CLI Weather App")
    parser.add_argument("city", nargs="?", help="City name")
    parser.add_argument("--forecast", "-f", action="store_true", help="Show forecast")
    parser.add_argument("--units", choices=["metric", "imperial"], default="metric")

    args = parser.parse_args()

    if not args.city:
        show_about()
        return

    try:
        current = fetch_current(args.city, args.units)
        show_current(current)

        if args.forecast:
            forecast = fetch_forecast(args.city, args.units)
            show_forecast(forecast)

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/] {e}")


if __name__ == "__main__":
    main()
