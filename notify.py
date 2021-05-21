import notify2
import rates

def notify():
    ICON_PATH = "/home/lobasov/PycharmProjects/notify/images/icon.svg"

    # Получаем текущий курс
    bitcoin = rates.fetch_bitcoin()

    # Инициализируем d-bus соединение
    notify2.init("Ух, ты! Сообщение...")

    # Создаём Notification-объект
    notify_obj = notify2.Notification("Notifier", icon = ICON_PATH)

    # Устанавливаем уровень срочности
    notify_obj.set_urgency(notify2.URGENCY_NORMAL)

    # Устанавливаем задержку
    notify_obj.set_timeout(10000)

    result = '\nBTC Price: {0} \nРыночная капитализация: {1}'.format(*bitcoin)

    # Обновляем содержимое
    notify_obj.update("Текущий курс", result)

    # Показываем уведомление
    notify_obj.show()

    print(result)


notify()
