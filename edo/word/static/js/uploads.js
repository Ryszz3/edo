/*
 * ============================================================
 *  ДЛЯ НОВИЧКОВ: ЧТО ТУТ ПРОИСХОДИТ?
 * ============================================================
 *
 *  Эта программа «вешает» обработчики на кнопки в карточках
 *  файлов. Когда пользователь нажимает «Согласовать»,
 *  «Отказать» или «Обработать», браузер отправляет AJAX-запрос
 *  на сервер. AJAX — это способ отправить данные без
 *  перезагрузки всей страницы.
 *
 *  Основные понятия:
 *  - document.querySelectorAll('.имя-класса') — найти все
 *    элементы с указанным CSS-классом.
 *  - addEventListener('click', функция) — «слушатель»: когда
 *    на элемент кликнут, вызовется функция.
 *  - fetch(url, настройки) — отправить HTTP-запрос на сервер.
 *  - .then(функция) — «когда запрос завершится, сделай это».
 *  - .catch(функция) — «если запрос упал с ошибкой, сделай это».
 *
 *   Структура скрипта:
 *   1. Получаем CSRF-токен (защита Django от подделки запросов)
 *   2. Настраиваем кнопки «Согласовать / Отказать»
 *   3. Настраиваем кнопки «Обработать»
 * ============================================================
 */

(function () {
    'use strict';

    // -------------------------------------------------
    // 1. ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
    // -------------------------------------------------

    /**
     * Достаёт CSRF-токен из <meta> тега или из скрытого поля формы.
     * Django требует этот токен при любом POST-запросе —
     * это защита от атак, когда злоумышленник с чужого сайта
     * пытается отправить форму от вашего имени.
     */
    function getCsrfToken() {
        var meta = document.querySelector('meta[name="csrf-token"]');
        if (meta && meta.getAttribute('content')) {
            return meta.getAttribute('content');
        }
        var input = document.querySelector('[name=csrfmiddlewaretoken]');
        if (input && input.value) {
            return input.value;
        }
        return null;
    }

    // -------------------------------------------------
    // 2. КНОПКИ «СОГЛАСОВАТЬ» / «ОТКАЗАТЬ»
    // -------------------------------------------------

    /**
     * Ищем все кнопки с классом js-publish.
     * У каждой такой кнопки есть два data-атрибута:
     *   data-id     — первичный ключ (pk) записи в базе
     *   data-action — строка "publish" или "unpublish"
     *
     * При клике отправляем POST-запрос с FormData.
     * Сервер сохраняет изменения в базу и возвращает
     * обновлённую HTML-страницу.
     *
     * ПОСЛЕ успешного ответа от сервера — перезагружаем
     * страницу, чтобы пользователь увидел реальные данные
     * из базы, а не догадки фронтенда.
     */
    var publishButtons = document.querySelectorAll('.js-publish');

    publishButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {

            // --- Читаем данные из кнопки ---
            var fileId = btn.getAttribute('data-id');
            var action = btn.getAttribute('data-action');

            // --- Визуальная обратная связь: кнопка «загружается» ---
            btn.classList.add('loading');

            // --- Собираем данные для отправки (как HTML-форма) ---
            var formData = new FormData();
            formData.append('csrfmiddlewaretoken', getCsrfToken());
            formData.append(action, fileId);
            // ↑ ключ — "publish" или "unpublish" (сервер ждёт именно такой параметр)

            // --- Отправляем AJAX-запрос ---
            fetch('', {
                method: 'POST',
                body: formData
            })
                .then(function () {
                    // Сервер ответил успешно — перезагружаем страницу,
                    // чтобы отобразить актуальное состояние из базы данных
                    window.location.reload();
                })
                .catch(function (error) {
                    btn.classList.remove('loading');
                    console.error(error);
                });
        });
    });

    // -------------------------------------------------
    // 3. КНОПКИ «ОБРАБОТАТЬ»
    // -------------------------------------------------

    /**
     * Ищем все кнопки с классом js-process.
     * У каждой такой кнопки есть data-id — первичный ключ записи.
     *
     * При клике отправляем JSON на адрес /process-file-ajax/.
     * Сервер ждёт объект вида: { file_index: число }
     */
    var processButtons = document.querySelectorAll('.js-process');

    processButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {

            // --- Читаем данные из кнопки ---
            var fileId = btn.getAttribute('data-id');

            // --- Визуальная обратная связь ---
            btn.classList.add('loading');

            // --- Отправляем AJAX-запрос с JSON-телом ---
            fetch('/process-file-ajax/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken()
                    // ↑ CSRF можно передать либо в теле (FormData),
                    //   либо в заголовке X-CSRFToken
                },
                // JSON.stringify превращает объект JS в строку JSON
                body: JSON.stringify({
                    file_index: parseInt(fileId, 10)
                })
            })
                .then(function () {
                    btn.classList.remove('loading');
                })
                .catch(function (error) {
                    btn.classList.remove('loading');
                    console.error(error);
                });
        });
    });

})();
