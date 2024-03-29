# GFY, dir.bg

## В опит за борба с цензурата

Предназначението на този софтуер е да може да се споделят уеб адреси, абревиатури на организации, имена на хора, емотикони и каквото още се сетите на латиница. Всичко, което попада под цензурата на dir.bg, прикрита зад червения надпис "Моля, пишете само на български език в коментара." за да не можем да публикуваме препратки към други сайтове.

На всеизвестния в България сайт не му е достатъчно да трие коментари в опит да спре разпространението на непопулярни мнения.
Не им е достатъчно и да блокират IP адреси. Лесно преодолимо обаче.

От известно време публикуването на коментари, които съдържат букви от английката азбука е забранено, като по този начин предотвратяват публикуването и на уеб адреси. При опит, просто ти се казва, че трябва да пишеш на кирилица.

Това възпрепятства споделянето на информация от различни източници между потребителите на сайта, за по-широко разглеждане на гледните точки - други новинарски сайтове, социални мрежи, сайтове за видео като [YouTube](https://www.youtube.com/)   или [Rumble](https://rumble.com/).

## Опит за заобикаляне на проблема

Метода е прост ­- превръщане на текста в [HTML entities](https://www.w3schools.com/charsets/ref_html_entities_4.asp).

Това са символи, които  нормално са част от кода на HTML документа ( уеб страницата), които определят, как ще бъде третирана всяка част от него. Към тези символи са добавени и много други с течение на времето, защото нуждата от тях е растяла.

По-важното е, че абсолютно всеки символ в документа, както кодиращите символи, така и текста, който е видим за нас, могат да се представят посредством HTTP entities.

Добавката работи, като превръща всеки символ подаден към нея, в неговия UTF-8 код в десетичен формат - 'L' непример има стойност 76, към която се прикрепят в началото и в края съответните символи, за да се преобразува до `&#76;`, която кодировка е напълно разбираема за браузъра.
И както виждате, в тази кодировка **не присътват** символи от английската или която и да е друга азбука. Системата на dir.bg не би трябвало да се оплаква от тях.

Например адресът https://www.google.com/ ще бъде конвертиран в следната последователност от HTML enteties:
`&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;&#119;&#119;&#119;&#46;&#103;&#111;&#111;&#103;&#108;&#101;&#46;&#99;&#111;&#109;&#47;`

Процесът е прост и директен. Направих елементарен тест, като публикувах усмивчица :D преди да започна да правя добавката. В последствие я ползвах за няколко публикации в dir.bg, докато я правех и всичко се получаваше, както би трябвало. В коментарите ми имаше това, което желаех.

При предишни опити при нормално изписване на текст на латиница това не беше възможно. Dir.bg не позволяваха дори един-единствен символ, за да се усмихнеш или просто за абревиатура.

## Пояснение

Това е резултат от близо 40 часа гледане на видео за Javascript,HTML и CSS. Затова, моля бъдете снизходителни. Това е първото нещо, което създавам с HTML, CSS и Javascript. При нередности, просто споделете.

Това е и първото ми ползване на GitHub и дано не съм  оплескал нещо :smile:

Програмите за Windows и Linux са елементарни, колкото и добавките за браузърите. Поле за въвеждане и бутон за конвертирането.

Отказах се да добавя добавката към контекстното меню в браузърите, защото това би означавало тя да наблюдава за всяко маркиране на текст, което на мен не ми харесва - смятам го за излишна намеса в живота ви. А и едва ли ще се ползва толкова често, че да да са пречка две кликвания с мишката.

В този си вид работи при мен. Тестван на четири браузъра - Firefox, Librewolf, Google Chrome и Brave.
Chrome и Firefox са най-използваните браузъри и не ме е грижа за останалите. Не ме е грижа още, че казвам не ме е грижа. :wink:
Почти всички други са базирани на тях, включително MS Edge, който също се присъедини към фамилята на Chromium браузърите.

## Как се използват добавките и програмата

Употребата им е проста.
Копирате желания текст, отваряте приложението, поставяте го в полето за въвеждане или собственоръчно написвате нещо там и натискате единствения бутон.
Конвертирания текст ще се копира автоматично в клипборда на операционната система и можете да го добавите към коментара си в dir.bg.
След което публикувате коментара си.
При четене на коментарите, тези кодове ще се представят като нормални символи на латиница - уеб адреси, имена, абревиатури, емотиконки, каквото сте искали да напишете, но не сте могли.

## Инсталация

### Windows, Linux

Програмата за  Windows както и тази за Linux не се инсталират.Просто я стартирате. Можете да я преместите където пожелаете и да направите препратка към нея, която да добавите към останалите програми в лентата на задачите. Добра идея би било, след това да присъедините клавишна комбинация за стартирането ѝ. Можете да си я носите и на флашка.

Можете да изтеглите изпълнимия файл за Windows от [тук](https://github.com/wavic/gfy-dir.bg/tree/master/packages/windows_standalone).

За Linux от [тук](https://github.com/wavic/gfy-dir.bg/blob/master/packages/linux_standalone/gfy-dir-bg).

В дясната част ще бутон за сваляне със стрелка надолу.

##### Програмата не прави промени по операционната система и не записва върху хард диска или системата ви никаква информация или файлове. Не събира и не изпраща данни.

### Firefox

- Добавката за Firefox е на този адрес: [https://addons.mozilla.org/en-US/firefox/addon/gfy-dir-bg/](https://addons.mozilla.org/en-US/firefox/addon/gfy-dir-bg/).
  Инсталирайте я. Потвърдете, когато бъдете запитани, дали искате да я инсталирате.

### Chrome

Добавката за Google Chrome ще трябва да инсталирате ръчно, защото не ми се дават пари на Google. Искат да им се плати, за да можеш да публикуваш добавки за браузъра им.

##### Ако някой разполага с Developer акаунт, свободно може да я публикува, ако има референция към адреса ѝ в GitHub. Пакета е в папка **packages/chrome_add-on**.

- Първо ще трябва да я свалите от  [тук](https://github.com/wavic/gfy-dir.bg/blob/master/packages/chrome_add-on/gfy-dir.bg_chrome.zip). В дясно ще видите бутон за downlad с подсказка "Download raw file".
  След като свалите архива ( той представлява просто сорс кода на добавката), създавате празна папка и го разархивирате в нея.
  Според програмата ви за разархивиране, тя или ще създаде папка с името на архива и ще постави съдържанието му в нея, или ще разархивира само съдържанието му в създадената от вас папка.
  Обърнете внимание в коя папка се намира файл с името **manifest.json**. На вас ви е нужна тази папка.
- След това отваряте менюто на браузъра ( трите точки, горе в дясно&vellip;). Избирате **Extensions** > **Manage extensions**.
  Горе в дясно ще видите **Developer mode**. Активирайте го.
  В ляво ще се появят три бутона. На вас ви трябва **Load unpacked** на който кликвате.
- Навигирате до папката в която е **manifest.json** и я посочвате. Добавката ще се инсталира.
- След това може да върнете обратно плъзгача за **Developer mode**
- В лентата за адресите на Chrome напишете **chrome://extensions/** и натиснете Enter или от менюто изберете отново  **Extensions** > **Manage extensions**.
  Ще видите инсталираната добавка. Натиснете бутона **Details** и по-надолу ще видите поле **Pin to toolbar** преместете плъзгача в активно състояниеи. С това ще добавите добавката към лентата с инструменти в дясно от адресната лента на Crome.

##### Добавките не събират и не изпращат данни

Поради тази причина можете безопасно да ги ползвате и в Incognito режим на браузъра.

### To Do

- Може би да направя програмата за Linux по-малка. Може би, като я пренапиша на Golang. Не ми се занимава със С или С++.
- Може би да включа вариант на програмата със светла тема, ако има достатъчно желаещи за такава.

### Лиценз

Софтуера е лицензиран под [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).
