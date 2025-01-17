## Порівняння ефективності

### Жадібний алгоритм

Жадібний алгоритм має часову складність \(O(n)\), де \(n\) — кількість номіналів монет. Він працює швидко для будь-якої суми, оскільки просто перебирає номінали монет від найбільшого до найменшого, додаючи монети до результату поки сума не буде досягнута.

**Переваги:**

- Простий у реалізації.
- Швидкий для невеликих і середніх сум.

**Недоліки:**

- Не завжди дає оптимальний результат для певних наборів номіналів монет.

### Алгоритм динамічного програмування

Алгоритм динамічного програмування має часову складність \(O(n \times k)\), де \(n\) — кількість номіналів монет, а \(k\) — сума. Він перебирає всі можливі способи формування суми, гарантуючи мінімальну кількість монет.

**Переваги:**

- Гарантовано знаходить мінімальну кількість монет.
- Працює для будь-яких наборів номіналів монет.

**Недоліки:**

- Може бути повільнішим для великих сум через більшу часову складність.

## Висновок

Жадібний алгоритм добре працює для наборів номіналів, які задовольняють специфічні умови (наприклад, коли кожен більший номінал можна подати сумою менших номіналів). Алгоритм динамічного програмування забезпечує оптимальний результат для будь-яких наборів номіналів, але може бути менш ефективним для дуже великих сум через свою складність.

Тож вибір алгоритму залежить від конкретної задачі та набору номіналів монет. Жадібний алгоритм може бути достатнім і більш ефективним у більшості реальних сценаріїв, тоді як алгоритм динамічного програмування слід використовувати, коли потрібно гарантувати мінімальну кількість монет.
