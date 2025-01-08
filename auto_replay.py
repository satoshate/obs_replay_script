import obspython as obs

# Глобальные переменные
hotkey_id = None
waiting_for_save = False  # Флаг ожидания сохранения буфера

# Функция, вызываемая при нажатии горячей клавиши
def save_replay_buffer_hotkey_callback(pressed):
    global waiting_for_save
    if pressed:
        obs.script_log(obs.LOG_INFO, "Горячая клавиша нажата.")

        if not obs.obs_frontend_replay_buffer_active():
            obs.script_log(obs.LOG_WARNING, "Буфер повтора не активен. Запускаем буфер повтора.")
            try:
                obs.obs_frontend_replay_buffer_start()
                obs.script_log(obs.LOG_INFO, "Буфер повтора запущен.")
            except AttributeError as e:
                obs.script_log(obs.LOG_WARNING, f"Ошибка при запуске буфера повтора: {e}")

            # Проверяем, активен ли буфер повтора после попытки запуска
            if not obs.obs_frontend_replay_buffer_active():
                obs.script_log(obs.LOG_WARNING, "Не удалось запустить буфер повтора.")
                return

        waiting_for_save = True  # Устанавливаем флаг ожидания
        try:
            obs.obs_frontend_replay_buffer_save()
            obs.script_log(obs.LOG_INFO, "Сохранение буфера повтора начато.")
        except AttributeError:
            obs.script_log(obs.LOG_WARNING, "Функция obs_frontend_replay_buffer_save недоступна.")

# Функция обработки событий OBS
def on_event(event):
    global waiting_for_save
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        if waiting_for_save:
            waiting_for_save = False  # Сбрасываем флаг ожидания
            obs.script_log(obs.LOG_INFO, "Буфер повтора сохранен.")

            # Добавляем задержку перед проверкой и перезапуском
            obs.timer_add(check_and_restart_replay_buffer, 500)  # 500 мс задержка
        else:
            obs.script_log(obs.LOG_WARNING, "Событие сохранения буфера повтора получено, но ожидание не установлено.")

# Функция для проверки состояния буфера повтора и перезапуска при необходимости
def check_and_restart_replay_buffer():
    try:
        obs.obs_frontend_replay_buffer_restart()
        obs.script_log(obs.LOG_INFO, "Буфер повтора перезапущен.")
    except AttributeError:
        # Если функция недоступна, используем альтернативный метод
        if not obs.obs_frontend_replay_buffer_active():
            obs.script_log(obs.LOG_INFO, "Буфер повтора не активен. Запускаем.")
            try:
                obs.obs_frontend_replay_buffer_start()
                obs.script_log(obs.LOG_INFO, "Буфер повтора запущен.")
            except AttributeError as e:
                obs.script_log(obs.LOG_WARNING, f"Ошибка при запуске буфера повтора: {e}")
        else:
            obs.script_log(obs.LOG_INFO, "Буфер повтора уже активен.")
    obs.timer_remove(check_and_restart_replay_buffer)


# Остальные функции без изменений
def script_description():
    return "Сохраняет текущий повтор и автоматически перезапускает буфер повтора по нажатию горячей клавиши."

def script_load(settings):
    global hotkey_id
    hotkey_id = obs.obs_hotkey_register_frontend(
        "auto_replay.save_and_restart",
        "Сохранить и перезапустить буфер повтора",
        save_replay_buffer_hotkey_callback
    )
    # Загружаем сохраненные горячие клавиши из настроек
    hotkey_array = obs.obs_data_get_array(settings, "auto_replay.save_and_restart")
    obs.obs_hotkey_load(hotkey_id, hotkey_array)
    obs.obs_data_array_release(hotkey_array)

    # Регистрируем обработчик событий
    obs.obs_frontend_add_event_callback(on_event)
    obs.script_log(obs.LOG_INFO, "Скрипт сохранения и перезапуска буфера повтора загружен.")

def script_unload():
    global hotkey_id
    if hotkey_id is not None:
        obs.obs_hotkey_unregister(hotkey_id)
        obs.script_log(obs.LOG_INFO, "Горячая клавиша успешно удалена при выгрузке скрипта.")

def script_save(settings):
    hotkey_array = obs.obs_hotkey_save(hotkey_id)
    obs.obs_data_set_array(settings, "auto_replay.save_and_restart", hotkey_array)
    obs.obs_data_array_release(hotkey_array)

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "description", "Инструкция", obs.OBS_TEXT_INFO)
    return props

def script_update(settings):
    pass

def script_defaults(settings):
    pass
