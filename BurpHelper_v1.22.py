from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IContextMenuFactory
from burp import IHttpRequestResponse
from burp import IMessageEditorController
from burp import IMessageEditorTabFactory
from burp import ITab
from burp import IMessageEditorTab
from burp import IScannerCheck
from burp import IScanIssue
from burp import IParameter
from javax import swing
from javax.swing.table import AbstractTableModel
from javax.swing.table import TableColumn
from java.awt import Color
from java.awt import Font
from java import awt
from java import lang
from java.awt.datatransfer import DataFlavor
from java.awt import Toolkit
from java.awt.datatransfer import StringSelection
import pickle
import java
from java.lang import *
from ctypes import *
import ctypes
import os
import subprocess
import time
import socket
import urllib
import re


class BurpExtender(IBurpExtender, IContextMenuFactory, IParameter, ITab):

  def registerExtenderCallbacks(self, callbacks):
    # Print information about the plugin, set extension name, setup basic stuff
    self.printHeader()
    callbacks.setExtensionName("BurpHelper")
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()
    callbacks.registerContextMenuFactory(self)
    # Create main panel with Components
    self._jTitleFont = Font("",Font.BOLD, 15)

    ##Current IP
    self._jLabelCurrentIPMainText = swing.JLabel()
    self._jLabelCurrentIPDesText = swing.JLabel()
    self._jLabelCurrentWanIpDes = swing.JLabel()
    self._jLabelCurrentLanIpDes = swing.JLabel()
    self._jLabelCurrentWanIp = swing.JLabel()
    self._jLabelCurrentLanIp = swing.JLabel()
    self._jCheckIPButton = swing.JButton("Check IP", actionPerformed=self.CheckIP)

    ##Proxy Setting

    self._jPAddButton = swing.JButton("Add", actionPerformed=self.PitemAdd)
    self._jPEditButton = swing.JButton("Edit", actionPerformed=self.PitemEdit)
    self._jPRemoveButton = swing.JButton("Remove", actionPerformed=self.PitemRemove)
    self._jLabelMainText = swing.JLabel()
    self._jLabelScanIPListen = swing.JLabel()
    
    self._jScanPanel = swing.JPanel()
    self._jScanPanel.setLayout(None)
    self._jTabledata = MappingTableModel(callbacks, self._jScanPanel)
    self._jTable = swing.JTable(self._jTabledata)
    self._jTablecont = swing.JScrollPane(self._jTable)
    self._jSeparator_first = swing.JSeparator(swing.JSeparator.HORIZONTAL);
    self._jSeparator_second = swing.JSeparator(swing.JSeparator.HORIZONTAL);
    
    ##Dashboard  
    self._jLabelDashboardText = swing.JLabel()
    self._jLabelDashboardDesText = swing.JLabel()
    self._jDTabledata = DashboardTableModel(callbacks, self._jScanPanel)
    self._jDTable = swing.JTable(self._jDTabledata)
    self._jDTablecont = swing.JScrollPane(self._jDTable)    


    # Configure GUI
    self._jLabelCurrentIPMainText.setText('Check Current IP ')
    self._jLabelCurrentIPMainText.setForeground(Color(228,127,0))
    self._jLabelCurrentIPMainText.setFont(self._jTitleFont)
    self._jLabelCurrentIPDesText.setText('You can check your current IP')
    self._jLabelCurrentWanIpDes.setText("Wan IP : ")
    self._jLabelCurrentLanIpDes.setText("Lan IP : ")


    self._jLabelMainText.setText('Proxy Server Setting')
    self._jLabelMainText.setForeground(Color(228,127,0))
    self._jLabelMainText.setFont(self._jTitleFont)
    self._jLabelScanIPListen.setText('You can set the proxy server, When the plugin is loading, Proxy Setting is initialized')
    self._jTable.getColumn("Name").setPreferredWidth(200)
    self._jTable.getColumn("IP").setPreferredWidth(150)
    self._jTable.getColumn("Port").setPreferredWidth(100)
    self._jTable.getColumn("Enabled").setPreferredWidth(50)

    
    self._jDTable.getColumn("URL").setPreferredWidth(180)
    self._jDTable.getColumn("Privilege").setPreferredWidth(130)
    self._jDTable.getColumn("ID").setPreferredWidth(100)
    self._jDTable.getColumn("Password").setPreferredWidth(100)
    self._jDTable.getColumn("Comment").setPreferredWidth(200)

    
    self._jScanPanel.setPreferredSize(awt.Dimension(1010,1010))


    self._jLabelDashboardText.setText('Target Site List')
    self._jLabelDashboardText.setForeground(Color(228,127,0))
    self._jLabelDashboardText.setFont(self._jTitleFont)
    self._jLabelDashboardDesText.setText('You can save the account list per site.')
    self._jDAddButton = swing.JButton("Add", actionPerformed=self.DitemAdd)
    self._jDEditButton = swing.JButton("Edit", actionPerformed=self.DitemEdit)
    self._jDRemoveButton = swing.JButton("Remove", actionPerformed=self.DitemRemove)
    self._jDIDCopyButton = swing.JButton("ID Copy", actionPerformed=self.DIDCopy)    
    self._jDPwCopyButton = swing.JButton("PW Copy", actionPerformed=self.DPwCopy)
    self._jDitemsDelete = swing.JButton("Clear", actionPerformed=self.DitemsDelete)
    self._jDURLConButton = swing.JButton("Open URL", actionPerformed=self.DOpenURL)

    # Configure locations
    self._jLabelCurrentIPMainText.setBounds(15, 10, 300, 20)
    self._jLabelCurrentIPDesText.setBounds(15, 32, 300, 20)
    self._jLabelCurrentWanIpDes.setBounds(15, 60, 60, 15)
    self._jLabelCurrentLanIpDes.setBounds(15, 80, 60, 15)
    self._jLabelCurrentWanIp.setBounds(80, 60, 100, 15)
    self._jLabelCurrentLanIp.setBounds(80, 80, 100, 15)
    self._jCheckIPButton.setBounds(190, 57, 90, 40)

    self._jSeparator_first.setBounds(15, 110, 900, 15) 

    self._jLabelMainText.setBounds(15, 120, 300, 20)
    self._jLabelScanIPListen.setBounds(15, 142, 500, 20)
    self._jPAddButton.setBounds(15, 170, 100, 30)
    self._jPEditButton.setBounds(15, 205, 100, 30)
    self._jPRemoveButton.setBounds(15, 240, 100, 30)
    self._jTablecont.setBounds(120, 170, 600, 150)
    self._jSeparator_second.setBounds(15, 335, 900, 15)    

    self._jLabelDashboardText.setBounds(15, 350, 300, 20)
    self._jLabelDashboardDesText.setBounds(15, 372, 300, 20)
    self._jDAddButton.setBounds(15, 400, 100, 30)
    self._jDEditButton.setBounds(15, 435, 100, 30)
    self._jDRemoveButton.setBounds(15, 470, 100, 30)
    self._jDURLConButton.setBounds(15, 505, 100, 30)
    self._jDIDCopyButton.setBounds(15, 540, 100, 30)
    self._jDPwCopyButton.setBounds(15, 575, 100, 30)
    self._jDTablecont.setBounds(120, 400, 750, 205)
    self._jDitemsDelete.setBounds(810, 375, 60, 25)
    
    # Component ADD
    self._jScanPanel.add(self._jLabelCurrentIPMainText)
    self._jScanPanel.add(self._jLabelCurrentIPDesText)
    self._jScanPanel.add(self._jLabelCurrentWanIp)
    self._jScanPanel.add(self._jLabelCurrentLanIp)
    self._jScanPanel.add(self._jLabelCurrentWanIpDes)
    self._jScanPanel.add(self._jLabelCurrentLanIpDes)
    self._jScanPanel.add(self._jCheckIPButton)
    self._jScanPanel.add(self._jLabelMainText)
    self._jScanPanel.add(self._jLabelScanIPListen)
    self._jScanPanel.add(self._jPAddButton)
    self._jScanPanel.add(self._jPEditButton)
    self._jScanPanel.add(self._jPRemoveButton)
    self._jScanPanel.add(self._jSeparator_first)
    self._jScanPanel.add(self._jTablecont)
    self._jScanPanel.add(self._jSeparator_second)
    self._jScanPanel.add(self._jLabelDashboardText)
    self._jScanPanel.add(self._jLabelDashboardDesText)
    self._jScanPanel.add(self._jDAddButton)
    self._jScanPanel.add(self._jDEditButton)
    self._jScanPanel.add(self._jDRemoveButton)
    self._jScanPanel.add(self._jDIDCopyButton)
    self._jScanPanel.add(self._jDPwCopyButton)
    self._jScanPanel.add(self._jDTablecont)
    self._jScanPanel.add(self._jDitemsDelete)
    self._jScanPanel.add(self._jDURLConButton)
	
    # ADD/EDIT Dialog Create Component
    ## PROXY

    self.panel = swing.JPanel()
    self.panel.setLayout(None)
    self.panel.setPreferredSize(awt.Dimension(200,140))
    self.DescriptionLabel = swing.JLabel()
    self.NameLabel = swing.JLabel()
    self.IPLabel = swing.JLabel()
    self.PortLabel = swing.JLabel()
    self.Nametext = swing.JTextField(50)
    self.IPtext = swing.JTextField(50)
    self.Porttext = swing.JTextField(50)

    ## ACOUNT
    self.Dpanel = swing.JPanel()
    self.Dpanel.setLayout(None)
    self.Dpanel.setPreferredSize(awt.Dimension(260,210))
    self.DDescriptionLabel = swing.JLabel()
    self.DURLLabel = swing.JLabel()
    self.DURLText = swing.JTextField(50)
    self.DPrivLabel = swing.JLabel()
    self.DPrivCombo = swing.JComboBox()
    self.DIDLabel = swing.JLabel()
    self.DIDText = swing.JTextField(50)
    self.DPassLabel = swing.JLabel()
    self.DPassText = swing.JTextField(50)
    self.DCommentLabel = swing.JLabel()
    self.DCommentText = swing.JTextField(50)
    self.DSubCommentLabel = swing.JLabel()
      
    # ADD/EDIT Dialog Configure locations 
    ## PROXY

    self.DescriptionLabel.setBounds(0,0,190,15)
    self.NameLabel.setBounds(5, 35, 50, 30)
    self.IPLabel.setBounds(5, 70, 50, 30)
    self.PortLabel.setBounds(5,105, 50, 30)
    self.Nametext.setBounds(60,35 , 150, 30)
    self.IPtext.setBounds(60,70 ,150, 30)
    self.Porttext.setBounds(60,105 , 150, 30)

    ## ACCOUNT
    self.DDescriptionLabel.setBounds(0,0, 200,10)
    
    self.DURLLabel.setBounds(5, 35, 70, 30)
    self.DURLText.setBounds(80, 35, 180, 30)
    self.DPrivLabel.setBounds(5, 70, 70, 30)
    self.DPrivCombo.setBounds(80, 70, 180, 30)
    self.DIDLabel.setBounds(5, 105, 70, 30)
    self.DIDText.setBounds(80, 105, 180, 30)
    self.DPassLabel.setBounds(5, 140, 70, 30)
    self.DPassText.setBounds(80, 140, 180, 30)
    self.DCommentLabel.setBounds(5, 175, 70, 15)
    self.DCommentText.setBounds(80, 175, 180, 30)
    self.DSubCommentLabel.setBounds(0,190,80,15)
    
    # ADD/EDIT Dialog Configure GUI
    ## PROXY
    
    self.DescriptionLabel.setText("Input your proxy server details.")
    self.NameLabel.setText("NAME : ")
    self.IPLabel.setText("IP : ")
    self.PortLabel.setText("PORT : ")

    ## ACCOUNT
    self.DDescriptionLabel.setText("Input your account details")
    self.DURLLabel.setText("URL : ")
    self.DPrivLabel.setText("Privilege : ")
    self.DIDLabel.setText("ID : ")
    self.DPassLabel.setText("Password : ")
    self.DCommentLabel.setText("Comment : ")
    self.DSubCommentLabel.setText("(Unique Text)");
    self.DPrivCombo.addItem("System Administrator")
    self.DPrivCombo.addItem("Staff Administrator")
    self.DPrivCombo.addItem("Internal Staff")
    self.DPrivCombo.addItem("Customer")
    self.DPrivCombo.addItem("The Lowest Privilege")
    self.DPrivCombo.addItem("ETC")
    self.DPrivCombo.setEditable(False) 
    
    # ADD/EDIT Dialog Component ADD
    ## PROXY
    self.panel.add(self.DescriptionLabel)
    self.panel.add(self.NameLabel)
    self.panel.add(self.IPLabel)
    self.panel.add(self.PortLabel)
    self.panel.add(self.Nametext);
    self.panel.add(self.IPtext);
    self.panel.add(self.Porttext);

    ## ACCOUNT
    self.Dpanel.add(self.DDescriptionLabel)
    self.Dpanel.add(self.DURLLabel)
    self.Dpanel.add(self.DURLText)
    self.Dpanel.add(self.DIDLabel)
    self.Dpanel.add(self.DIDText)
    self.Dpanel.add(self.DPassLabel)
    self.Dpanel.add(self.DPassText)
    self.Dpanel.add(self.DPrivLabel)
    self.Dpanel.add(self.DPrivCombo)
    self.Dpanel.add(self.DCommentLabel)
    self.Dpanel.add(self.DCommentText)
    self.Dpanel.add(self.DSubCommentLabel)

    # Setup Tabs
    self._jConfigTab = swing.JTabbedPane()
    self._jConfigTab.addTab("Smart Settings", self._jScanPanel)
    callbacks.addSuiteTab(self)
    return

  def CheckIP(self, e):
    lan = socket.gethostbyname(socket.gethostname())
    try:
      wan = re.search(re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'),urllib.urlopen('https://www.ipchicken.com').read()).group()
    except IOError:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "Cannot Connect dyndns server.. Check your Internet Connection", "Error", swing.JOptionPane.ERROR_MESSAGE, None );

    self._jLabelCurrentWanIp.setText(wan)
    self._jLabelCurrentLanIp.setText(lan)

    self._jCheckIPButton.setText("Refresh")


  def getTabCaption(self):
    return 'BurpHelper'

  def getUiComponent(self):
    return self._jConfigTab

  def printHeader(self):
    print '==================\nBurpHelper ver 1.22\n==================\nDeveloped by NELpos, Thanks to darkhi'

  def PitemAdd(self, e): 
    optionlist = ["Add", "Cancel"]
    self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel, self.panel, "Add Proxy Server", swing.JOptionPane.DEFAULT_OPTION, swing.JOptionPane.PLAIN_MESSAGE, None, optionlist, None)
    
    if self.result == swing.JOptionPane.OK_OPTION:
        Name = self.Nametext.getText()
        Ip = self.IPtext.getText()
        Port = self.Porttext.getText()

        #Check duplicate
        tmp = self._jTabledata.getIds()
        for item in tmp:
          if item == Name:
            swing.JOptionPane.showMessageDialog(self._jScanPanel, "This 'Name' which you entered already exists. Please enter another 'Name'", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
            return;

        #Make List
        addData = [Name, Ip, Port]
        self._jTabledata.add_mapping(Name, Ip, Port)
    
        self.Nametext.setText("")
        self.IPtext.setText("")
        self.Porttext.setText("")
    
  def PitemEdit(self, e):
    rows = self._jTable.getSelectedRows().tolist()

    if len(rows) == 0:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select one in order to edit", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      return
    elif len(rows) > 1:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select only one", "Error", swing.JOptionPane.ERROR_MESSAGE, None );
      return
    else:
      Ids = self._jTabledata.getIds()
      name = Ids[rows[0]]
      tmplist = self._jTabledata.getValue(name)

      #Get Item Value
      ip =  tmplist[0]
      port = tmplist[1]
      enabled = tmplist[2]

      self.Nametext.setText(name)
      self.IPtext.setText(ip)
      self.Porttext.setText(port)

      optionlist = ["Edit", "Cancel"]
      self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel, self.panel, "Edit Proxy Server", swing.JOptionPane.DEFAULT_OPTION, swing.JOptionPane.PLAIN_MESSAGE, None, optionlist, None)

      if self.result == swing.JOptionPane.OK_OPTION:
          Name = self.Nametext.getText()
          Ip = self.IPtext.getText()
          Port = self.Porttext.getText()
          EditData = [Name, Ip, Port, enabled]

          self._jTabledata.editValue(EditData, rows[0])

          self.Nametext.setText("")
          self.IPtext.setText("")
          self.Porttext.setText("")

  def PitemRemove(self, e):
    self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel,"Are you sure you want to remove this Name?", "Remove", swing.JOptionPane.YES_NO_OPTION, swing.JOptionPane.QUESTION_MESSAGE,  None,None, None)

    if self.result == swing.JOptionPane.OK_OPTION:
      rows = self._jTable.getSelectedRows().tolist()
      self._jTabledata.del_rows(rows)


  def DitemAdd(self, e):
    optionlist = ["Add", "Cancel"]
    self.DURLText.setText("")
    self.DIDText.setText("")
    self.DPassText.setText("")
    self.DCommentText.setText("")
    self.DPrivCombo.setSelectedIndex(0)

    self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel, self.Dpanel, "Add Site", swing.JOptionPane.DEFAULT_OPTION, swing.JOptionPane.PLAIN_MESSAGE, None, optionlist, None)
    if self.result == swing.JOptionPane.OK_OPTION:
        Url = self.DURLText.getText()
        Priv = self.DPrivCombo.getSelectedItem()
        Id = self.DIDText.getText()
        Pw = self.DPassText.getText()
        Com = self.DCommentText.getText()

        #Check duplicate
        tmp = self._jDTabledata.getIds()
        for item in tmp:
          if item == Com:
            swing.JOptionPane.showMessageDialog(self._jScanPanel, "This 'Comment' which you entered already exists. Please enter another 'Comment'", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
            return;
    
        #Make List
        addData = [Url, Priv, Id, Pw, Com]
        self._jDTabledata.add_mapping(Url, Priv, Id, Pw, Com)
     

  def DitemEdit(self, e):
    rows = self._jDTable.getSelectedRows().tolist()

    if len(rows) == 0:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select one in order to edit", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      return
    elif len(rows) > 1:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select only one", "Error", swing.JOptionPane.ERROR_MESSAGE, None );
      return
    else:
      Ids = self._jDTabledata.getIds()
      com = Ids[rows[0]]
      tmplist = self._jDTabledata.getValue(com)

      #Get Item Value
      url =  tmplist[0]
      priv = tmplist[1]
      Id = tmplist[2]
      Pw = tmplist[3]
      Com = com

      self.DURLText.setText(url)
      selcount =  self.DPrivCombo.getItemCount()
      for i in range(0, selcount) :
        if self.DPrivCombo.getItemAt(i) == priv:
          self.DPrivCombo.setSelectedIndex(i)
          break

      self.DIDText.setText(Id)
      self.DPassText.setText(Pw)
      self.DCommentText.setText(Com)

      optionlist = ["Edit", "Cancel"]
      self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel, self.Dpanel, "Edit Site", swing.JOptionPane.DEFAULT_OPTION, swing.JOptionPane.PLAIN_MESSAGE, None, optionlist, None)

      if self.result == swing.JOptionPane.OK_OPTION:
          url = self.DURLText.getText()
          Priv = self.DPrivCombo.getSelectedItem()
          Id = self.DIDText.getText()
          Pw = self.DPassText.getText()
          Com = self.DCommentText.getText()
          
          EditData = [url, Priv, Id, Pw, Com]
          self._jDTabledata.editValue(EditData, rows[0])
          self.DURLText.setText("")
          self.DIDText.setText("")
          self.DPassText.setText("")
          self.DCommentText.setText("")

  def DitemRemove(self, e):
    self.result = swing.JOptionPane.showOptionDialog(self._jScanPanel,"Are you sure you want to remove this Item?", "Remove", swing.JOptionPane.YES_NO_OPTION, swing.JOptionPane.QUESTION_MESSAGE,  None,None, None)

    if self.result == swing.JOptionPane.OK_OPTION:
      rows = self._jDTable.getSelectedRows().tolist()
      self._jDTabledata.del_rows(rows)
    
  def DIDCopy(self, e):
    rows = self._jDTable.getSelectedRows().tolist()
    if len(rows) == 0:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select one in order to open URL", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      return
    elif len(rows) > 1:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select only one item", "Error", swing.JOptionPane.ERROR_MESSAGE, None );
      return
    else:
      Ids = self._jDTabledata.getIds()
      com = Ids[rows[0]]
      tmplist = self._jDTabledata.getValue(com)
      ID = tmplist[2]
      toolkit = Toolkit.getDefaultToolkit()
      clipboard = toolkit.getSystemClipboard()
      clipboard.setContents(StringSelection(ID), None)
      swing.JOptionPane.showMessageDialog(self.panel, "ID is copied to clipboard, Use Ctrl+V into the ID form", "Success", swing.JOptionPane.INFORMATION_MESSAGE, None);

  def DPwCopy(self, e):
    rows = self._jDTable.getSelectedRows().tolist()
    if len(rows) == 0:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select one in order to open URL", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      return
    elif len(rows) > 1:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select only one item", "Error", swing.JOptionPane.ERROR_MESSAGE, None );
      return
    else:
      Ids = self._jDTabledata.getIds()
      com = Ids[rows[0]]
      tmplist = self._jDTabledata.getValue(com)
      Pw = tmplist[3]
      toolkit = Toolkit.getDefaultToolkit()
      clipboard = toolkit.getSystemClipboard()
      clipboard.setContents(StringSelection(Pw), None)
      swing.JOptionPane.showMessageDialog(self.panel, "Password is copied to clipboard, Use Ctrl+V into the password form", "Success", swing.JOptionPane.INFORMATION_MESSAGE, None);
      

  def DitemsDelete(self, e):
    if not os.path.isdir('c:\\burphelper'):
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You don't have list files.", "Error", swing.JOptionPane.ERROR_MESSAGE, None);          
    else:
      if os.path.isfile("c:\\burphelper\\sitelist"):
            swing.JOptionPane.showMessageDialog(self.panel, "Dashboard is cleared, and delete the sitelist file ", "Success", swing.JOptionPane.INFORMATION_MESSAGE, None);
            os.remove("c:\\burphelper\\sitelist")

            #clear rows
            rows = self._jDTabledata.getRowCount()
            self._jDTabledata.table_clear()
      else:
         swing.JOptionPane.showMessageDialog(self._jScanPanel, "You don't have list files.", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      

    #self._jDTabledata

  def DOpenURL(self, e):
    rows = self._jDTable.getSelectedRows().tolist()
    if len(rows) == 0:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select one in order to open URL", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
      return
    elif len(rows) > 1:
      swing.JOptionPane.showMessageDialog(self._jScanPanel, "You have to select only one item", "Error", swing.JOptionPane.ERROR_MESSAGE, None );
      return
    else:
      Ids = self._jDTabledata.getIds()
      com = Ids[rows[0]]
      tmplist = self._jDTabledata.getValue(com)
	  
      if tmplist[0].find('http://') == -1 :
	  url = "http://" + tmplist[0]
      else:
	  url = tmplist[0]			  
      openURLCommand = 'start "%s"' %url
      runURL = subprocess.Popen(openURLCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

class MappingTableModel(AbstractTableModel):
    def __init__(self, callbacks, panel):
        AbstractTableModel.__init__(self)
        self.columnnames = ["Name", "IP", "Port", "Enabled"]
        self.mappings = dict()
        self.idorder = list()
        self.lastadded = None
        self.callbacks = callbacks
        self.loadMapping()       

        self.panel = panel      
        #Item list load
        self.itemload()

        #Proxy Setting initialize 
        self.set_proxy_disable(1)

    def itemload(self):
        
        #temp folder and file create
        if not os.path.isdir('c:\\burphelper'):
          os.mkdir('c:\\burphelper')
        else:
          if os.path.isfile("c:\\burphelper\\proxylist"):
            f = open("c:\\burphelper\\proxylist", "r")
            while True:
                lines = f.readline()
                if not lines: break
                item = lines.split('/')
                if len(item) > 1:
                  self.add_mapping(item[0], item[1], item[2])
            f.close()
                
    def itemsave(self):
        f = open("c:\\burphelper\\proxylist", "w")
        for item in self.idorder:
          tmp = self.mappings[item]
          savetext = item + '/' + tmp[0] + '/' + tmp[1] + '/\n'
          f.write(savetext)
        f.close()
    def getColumnCount(self):
        return len(self.columnnames)

    def getRowCount(self):
        return len(self.mappings)

    def getColumnName(self, col):
        return self.columnnames[col]

    def getValueAt(self, row, col):
        # Load Dictionary
        tmplist = self.mappings[self.idorder[row]]
        if col == 0:
            return self.idorder[row]
        elif col == 1: 
            return tmplist[0]
        elif col == 2: 
            return tmplist[1]
        else:
            if tmplist[2] == 0:
              return java.lang.Boolean(0)
            else:
              return java.lang.Boolean(1)
      
    def getColumnClass(self, idx):
        if idx ==0 or idx==1 or idx==2: 
          return str
        elif idx == 3:
          #Boolean convert Checkbox
          return java.lang.Class.getClass(self.getValueAt(0, idx))
      
    def isCellEditable(self, row, col):
        if col>2:           #only checkbox editable
          return True
        else:
          return False    
      
    def add_mapping(self, name, ip, port):
        if name not in self.mappings:
            self.idorder.append(name)
        self.mappings[name] = [ip, port, 0]
        self.lastadded = name
        self.fireTableDataChanged()
        self.saveMapping()
        self.itemsave()

    def set_lastadded_content(self, content):
        self.mappings[self.lastadded] = content
        self.fireTableDataChanged()

    def del_rows(self, rows):
        rows.sort()
        deleted = 0
        for row in rows:
            delkey = self.idorder[row - deleted]
            del self.mappings[delkey]
            if delkey == self.lastadded:
                self.lastadded = None
            if row - deleted > 0:
                self.idorder = self.idorder[:row - deleted] + self.idorder[row + 1 - deleted:]
            else:
                self.idorder = self.idorder[1:]
            self.fireTableRowsDeleted(row - deleted, row - deleted)
            deleted = deleted + 1
        self.saveMapping()
        self.itemsave()

    def editValue(self, val, row):
        tmp = [val[1], val[2], val[3]]
        del self.mappings[self.idorder[row]]
        self.idorder[row] = val[0];
        self.mappings[val[0]] = tmp
        self.fireTableDataChanged()
        self.saveMapping()
        self.itemsave()

    def set_proxy_enable(self, ipport):
      #Registry setting
      proxyServer='reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v "ProxyServer" /t REG_SZ /d "%s" /f' %ipport
      proxyEnable = 'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v "ProxyEnable" /t REG_DWORD /d 1 /f'

      run1 = subprocess.Popen(proxyServer, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
      run2 = subprocess.Popen(proxyEnable, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

      #registry change check!
      while True:
          rcheckcmd ='reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v "ProxyEnable"' 
          result = subprocess.Popen(rcheckcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
          resulttext =  list(result.communicate())
          data = resulttext[0]
          value = data[data.find("DWORD")+9:data.find("DWORD")+12]
          if value == "0x1":
            break;  
      return 1

    def set_proxy_disable(self, dtype):      
      disablevalue = 'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v "ProxyEnable" /t REG_DWORD /d 0 /f'         
      run1 =subprocess.Popen(disablevalue, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

      #registry change check
      while True:        
          rcheckcmd ='reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v "ProxyEnable"'
          result = subprocess.Popen(rcheckcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
          resulttext =  list(result.communicate())         
          data = resulttext[0]
          value = data[data.find("DWORD")+9:data.find("DWORD")+12]  
          if value == "0x0":
            break;
      
      # code here     
      if dtype == 1 : #initialize
        self.internet_refresh(3)
      elif dtype == 2:
        self.internet_refresh(2)
            
    def internet_refresh(self, ptype):
        #loading wininet.dll
        dll_name="wininet.dll"
        wininet = ctypes.CDLL(dll_name)
        wininet.InternetSetOptionW.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

        INTERNET_OPTION_REFRESH = 37
        INTERNET_OPTION_SETTINGS_CHANGED = 39
        
        #Internet Setting Refresh and change
        changed_result = wininet.InternetSetOptionW(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        refresh_result = wininet.InternetSetOptionW(0, INTERNET_OPTION_REFRESH, 0, 0)
        
        
        if refresh_result ==0 or changed_result ==0:
          swing.JOptionPane.showMessageDialog(self.panel, "Fail to set.. Please try again", "Error", swing.JOptionPane.ERROR_MESSAGE, None);
          self.set_proxy_disable()
        else:
          if ptype == 1:    #enable
            swing.JOptionPane.showMessageDialog(self.panel, "Proxy is enabled", "Success", swing.JOptionPane.INFORMATION_MESSAGE, None);
          elif ptype == 2:  #disable
            swing.JOptionPane.showMessageDialog(self.panel, "Proxy is disabled", "Success", swing.JOptionPane.INFORMATION_MESSAGE, None);
    
    def setValueAt(self, val, row, col):      
        #Checkbox Setting
        if col == 3:
            tmp =  self.mappings[self.idorder[row]]
            # check to uncheck(disable)
            if tmp[2] == 1:
              self.mappings[self.idorder[row]] = [tmp[0], tmp[1], 0]
              ptype = self.set_proxy_disable(2)
            
            # uncheck to check(enable)  
            else:
              for item in self.idorder:
                if item != self.mappings[self.idorder[row]]:
                  itemtmp = self.mappings[item]
                  self.mappings[item] = [itemtmp[0], itemtmp[1], 0]
              self.mappings[self.idorder[row]] = [tmp[0], tmp[1], 1]
              ipport = tmp[0] + ":" + tmp[1]
              ptype = self.set_proxy_enable(ipport)
              self.internet_refresh(ptype)                                     
        self.fireTableDataChanged()
        self.saveMapping()
        self.itemsave()
    def getIds(self):
        return self.idorder

    def getValue(self, ident):
        return self.mappings[ident]

    def containsId(self, msg):
        for ident in self.idorder:
            if msg.find(ident) >= 0:
                return True
        return False

    def saveMapping(self):
        self.callbacks.saveExtensionSetting("mappings", pickle.dumps(self.mappings))
        self.callbacks.saveExtensionSetting("idorder", pickle.dumps(self.idorder))
        self.callbacks.saveExtensionSetting("lastadded", pickle.dumps(self.lastadded))

    def loadMapping(self):
        storedMappings = self.callbacks.loadExtensionSetting("mappings")
        if isinstance(storedMappings, str):
            try:
                self.mappings = pickle.loads(storedMappings) or dict()
            except:
                self.mappings = dict()

        storedIdorder = self.callbacks.loadExtensionSetting("idorder")
        if isinstance(storedIdorder, str):
            try:
                self.idorder = pickle.loads(storedIdorder) or list()
            except:
                self.idorder = list()

        storedLastAdded = self.callbacks.loadExtensionSetting("lastadded")
        if isinstance(storedLastAdded, str):
            try:
                self.lastadded = pickle.loads(storedLastAdded)
            except:
                self.lastadded = None


class DashboardTableModel(AbstractTableModel):
    def __init__(self, callbacks, panel):
        AbstractTableModel.__init__(self)
        self.columnnames = ["URL", "Privilege", "ID", "Password", "Comment"]
        self.mappings = dict()
        self.idorder = list()
        self.lastadded = None
        self.callbacks = callbacks
        self.loadMapping()       

        self.panel = panel      
        #Item list load
        self.D_itemload()

    def D_itemload(self): 
        #temp folder and file create
        if not os.path.isdir('c:\\burphelper'):
          os.mkdir('c:\\burphelper')
        else:
          if os.path.isfile("c:\\burphelper\\sitelist"):
            f = open("c:\\burphelper\\sitelist", "r")
            while True:
                lines = f.readline()
                if not lines: break
                item = lines.split('/')
                if len(item) > 1:
                  self.add_mapping(item[0], item[1], item[2], item[3], item[4])
            f.close()
                
    def D_itemsave(self):
        f = open("c:\\burphelper\\sitelist", "w")
        for item in self.idorder:
          tmp = self.mappings[item]
          savetext = tmp[0] + '/' + tmp[1] + '/' + tmp[2] + '/' + tmp[3] + '/' + item + '/\n'
          f.write(savetext)
        f.close()
    def getColumnCount(self):
        return len(self.columnnames)

    def table_clear(self):
        self.mappings.clear()
        self.idorder[:] = []
        self.lastadded = None
        self.fireTableDataChanged()
        self.saveMapping()
        
    def getRowCount(self):
        return len(self.mappings)

    def getColumnName(self, col):
        return self.columnnames[col]

    def getValueAt(self, row, col):
        # Load Dictionary
        tmplist = self.mappings[self.idorder[row]]
        if col == 0:
            return tmplist[0]
        elif col == 1: 
            return tmplist[1]
        elif col == 2: 
            return tmplist[2]
        elif col == 3:
            mask = ""
            for i in range (1, len(tmplist[3])):
              mask = mask + "*"
            return mask
        else:
            return self.idorder[row]
      
    def getColumnClass(self, idx):
          return str
      
    def isCellEditable(self, row, col):
          return False
      
    def add_mapping(self, url, priv, Id, Pw, Com):
        if Com not in self.mappings:
            self.idorder.append(Com)
        self.mappings[Com] = [url, priv, Id, Pw, Com]
        self.lastadded = Com
        self.fireTableDataChanged()
        self.saveMapping()
        self.D_itemsave()

    def set_lastadded_content(self, content):
        self.mappings[self.lastadded] = content
        self.fireTableDataChanged()

    def del_rows(self, rows):
        rows.sort()
        deleted = 0
        for row in rows:
            delkey = self.idorder[row - deleted]
            del self.mappings[delkey]
            if delkey == self.lastadded:
                self.lastadded = None
            if row - deleted > 0:
                self.idorder = self.idorder[:row - deleted] + self.idorder[row + 1 - deleted:]
            else:
                self.idorder = self.idorder[1:]
            self.fireTableRowsDeleted(row - deleted, row - deleted)
            deleted = deleted + 1
        self.saveMapping()
        self.D_itemsave()

    def editValue(self, val, row):
        tmp = [val[0], val[1], val[2], val[3]]
        del self.mappings[self.idorder[row]]
        self.idorder[row] = val[4];
        self.mappings[val[4]] = tmp
        self.fireTableDataChanged()
        self.saveMapping()
        self.D_itemsave()
 
    def setValueAt(self, val, row, col):                                           
        self.fireTableDataChanged()
        self.saveMapping()
        self.D_itemsave()
    def getIds(self):
        return self.idorder

    def getValue(self, ident):
        return self.mappings[ident]

    def containsId(self, msg):
        for ident in self.idorder:
            if msg.find(ident) >= 0:
                return True
        return False

    def saveMapping(self):
        self.callbacks.saveExtensionSetting("mappings", pickle.dumps(self.mappings))
        self.callbacks.saveExtensionSetting("idorder", pickle.dumps(self.idorder))
        self.callbacks.saveExtensionSetting("lastadded", pickle.dumps(self.lastadded))

    def loadMapping(self):
        storedMappings = self.callbacks.loadExtensionSetting("mappings")
        if isinstance(storedMappings, str):
            try:
                self.mappings = pickle.loads(storedMappings) or dict()
            except:
                self.mappings = dict()

        storedIdorder = self.callbacks.loadExtensionSetting("idorder")
        if isinstance(storedIdorder, str):
            try:
                self.idorder = pickle.loads(storedIdorder) or list()
            except:
                self.idorder = list()

        storedLastAdded = self.callbacks.loadExtensionSetting("lastadded")
        if isinstance(storedLastAdded, str):
            try:
                self.lastadded = pickle.loads(storedLastAdded)
            except:
                self.lastadded = None
