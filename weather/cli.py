import argparse
from importlib.metadata import PackageNotFoundError, metadata

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from weather.api import fetch_current, fetch_forecast

console = Console()


def show_about():
    try:
        meta = metadata("weather-cli")
    except PackageNotFoundError:
        console.print("[red]Package metadata not found[/]")
        return

    ASCII_LOGO = r"""
   _      __           __  __           
  | | /| / /__ ___ _  / /_/ /  ___ ____
  | |/ |/ / -_) _ `/ / __/ _ \/ -_) __/
  |__/|__/\__/\_,_/  \__/_//_/\__/_/   
"""

    console.print(f"[yellow]{ASCII_LOGO}[/yellow]")

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
🌡️ Temp: [bold cyan]{data['main']['temp']}°[/]
🤗 Feels: [cyan]{data['main']['feels_like']}°[/]
💧 Humidity: [cyan]{data['main']['humidity']}%[/]
☁️ {data['weather'][0]['description'].capitalize()}
""",
        title=f"[yellow]Weather in {data['name']}",
        border_style="blue",
    )
    console.print(panel)


def show_forecast(data):
    table = Table(title="5-Day Forecast", header_style="bold magenta")
    table.add_column("Date")
    table.add_column("Temp (°)")
    table.add_column("Condition")

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
