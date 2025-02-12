
Select = '''QPushButton::pressed {
    border-width: 5px;
    border-radius: 20px;
    background-color: gold;
    border-style: inset;
}
    '''
Sign_in = '''
	color: white;
	background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));
	border-radius: 20px;
'''
QSS1 = '''
QWidget {
    border: fixed
    border-radius: 20px ;
    background-color: rgb(238, 187, 136);
}
QListWidget
{
    border : fixed;
    background : lightgreen;
}
QListWidget QScrollBar{
    background : red;
}


QListView::item:selected{
background : orange;
}
QLabel {
    background-color: cyan;
    font: bold 17px "Century Gothic";
    color: black;

}
QPushButton::indicator::checked {
    border: 1px; 
    border-color: green;
    background-color: green;
    border-radius: 7px;
}

QLabel { 
    font: 17px ""Century Gothic";
} 
'''

QSS_OK = '''
QPushButton {
    background-color: rgb(0, 0, 0); 
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    min-width: 10em;
    padding: 6px;
}


QSS_TextCardQuestion = QLabel { 
    font: bold 15px "Montserrat";
}

QSS_TextResult = QLabel {
    font: italic 15px "Montserrat";
}

QSS_TextHeader = =QLabel {
    font: 15px ;
} '''

