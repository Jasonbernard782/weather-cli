import argparse

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from weather.api import fetch_current, fetch_forecast

console = Console()

def show_current(data):
    panel = Panel(
        f"""[magenta]
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
    parser.add_argument("city", help="City name")
    parser.add_argument("--forecast", "-f", action="store_true", help="Show forecast")
    parser.add_argument("--units", choices=["metric", "imperial"], default="metric")

    args = parser.parse_args()

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
