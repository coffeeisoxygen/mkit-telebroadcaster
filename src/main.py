from nicegui import ui


# ----------------------
# Sidebar Component
# ----------------------
def sidebar():
    with ui.column().classes("w-64 bg-gray-200 p-4 h-full fixed"):
        ui.label("📢 Telegram Broadcast").classes("text-lg font-bold mb-4")
        ui.link("Dashboard", "/").classes("block p-2 hover:bg-gray-300 rounded")
        ui.link("Config", "/config").classes("block p-2 hover:bg-gray-300 rounded")
        ui.link("Logs", "/logs").classes("block p-2 hover:bg-gray-300 rounded")


# ----------------------
# Pages
# ----------------------
@ui.page("/")
def dashboard_page():
    sidebar()
    with ui.column().classes("ml-72 p-4"):
        ui.label("📊 Dashboard").classes("text-2xl font-bold mb-4")
        ui.label("Status Bot: ✅ Online").classes("mb-2")
        ui.label("Last Broadcast: -")
        ui.button(
            "Broadcast Sekarang",
            on_click=lambda: ui.notify("Broadcast manual dijalankan!", type="positive"),
        )


@ui.page("/config")
def config_page():
    sidebar()
    with ui.column().classes("ml-72 p-4"):
        ui.label("⚙️ Config").classes("text-2xl font-bold mb-4")
        ui.input("Token Bot")
        ui.input("Channel ID")
        ui.textarea("SQL Query").classes("w-full h-32")
        ui.button(
            "Simpan Config",
            on_click=lambda: ui.notify("Config disimpan!", type="positive"),
        )


@ui.page("/logs")
def logs_page():
    sidebar()
    with ui.column().classes("ml-72 p-4"):
        ui.label("📝 Logs").classes("text-2xl font-bold mb-4")
        ui.label("Belum ada log.")


# ----------------------
# Run
# ----------------------
ui.run(port=8080, title="Telegram Broadcast Dashboard")
