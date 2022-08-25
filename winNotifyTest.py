from plyer import notification

# notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False)

notification.notify(title="周计划过期提醒", message="计划1 过期时间还剩1天\n计划2 过期时间还剩10天", app_name='周计划提醒系统',
                    timeout=3, ticker='你有未完成周计划', toast=False)
