# -*- coding: utf-8 -*-

from PyQt5 import QtCore
import pandas as pd


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError,):
                return QtCore.QVariant()
        return super(PandasModel, self).headerData(section, orientation, role)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if not index.isValid():
            return QtCore.QVariant()
        if index.row() == 0:
            return QtCore.QVariant(self._df.columns.values[index.column()])
        return QtCore.QVariant(str(self._df.iloc[index.row() - 1, index.column()]))

    def setData(self, index, value, role):
        if index.row() == 0:
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            self._df.columns.values[index.column()] = value
            self.headerDataChanged.emit(QtCore.Qt.Horizontal, index.column(), index.column())
        else:
            col = self._df.columns[index.column()]
            row = self._df.index[index.row() - 1]
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            else:
                dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
                self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index) + 1

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending=order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()
