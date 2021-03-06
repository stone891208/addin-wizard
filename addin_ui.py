#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Sep 19 12:33:19 2011

import wx

# begin wxGlade: extracode
_msize = wx.Size(700, 550)
_msize = wx.Size(700, 550)
# end wxGlade



class AddinMakerWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AddinMakerWindow.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.full_app_panel = wx.Panel(self, -1)
        self.bottom_buttons_pane = wx.Panel(self.full_app_panel, -1)
        self.propsheet_panel = wx.Panel(self.full_app_panel, -1)
        self.tabs_notebook = wx.Notebook(self.propsheet_panel, -1, style=0)
        self.project_items_pane = wx.Panel(self.tabs_notebook, -1)
        self.item_property_panel = wx.Panel(self.project_items_pane, -1)
        self.project_settings_pane = wx.Panel(self.tabs_notebook, -1)
        self.logo_panel = wx.Panel(self.propsheet_panel, -1)
        self.properties_rows_holder_staticbox = wx.StaticBox(self.project_settings_pane, -1, "Project Properties:")
        self.title_panel = wx.Panel(self.full_app_panel, -1)
        self.title_label = wx.StaticText(self.title_panel, -1, "Python Add-In Wizard", style=wx.ALIGN_RIGHT)
        self.title_divider_line = wx.StaticLine(self.full_app_panel, -1)
        self.logo_bitmap = wx.StaticBitmap(self.logo_panel, -1, wx.Bitmap("images\\AddInDesktop64.png", wx.BITMAP_TYPE_ANY))
        self.folder_label = wx.StaticText(self.project_settings_pane, -1, "Working Folder:", style=wx.ALIGN_RIGHT)
        self.folder_button = wx.Button(self.project_settings_pane, -1, "Select Folder...")
        self.product_label = wx.StaticText(self.project_settings_pane, -1, "Select Product:", style=wx.ALIGN_RIGHT)
        self.product_combo_box = wx.ComboBox(self.project_settings_pane, -1, choices=["ArcMap", "ArcGlobe", "ArcScene", "ArcCatalog"], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.static_line_1 = wx.StaticLine(self.project_settings_pane, -1)
        self.project_name_label = wx.StaticText(self.project_settings_pane, -1, "Name*:", style=wx.ALIGN_RIGHT)
        self.project_name = wx.TextCtrl(self.project_settings_pane, -1, "")
        self.project_version_label = wx.StaticText(self.project_settings_pane, -1, "Version*:", style=wx.ALIGN_RIGHT)
        self.project_version = wx.TextCtrl(self.project_settings_pane, -1, "")
        self.project_company_label = wx.StaticText(self.project_settings_pane, -1, "Company:", style=wx.ALIGN_RIGHT)
        self.project_company = wx.TextCtrl(self.project_settings_pane, -1, "")
        self.project_description_label = wx.StaticText(self.project_settings_pane, -1, "Description:", style=wx.ALIGN_RIGHT)
        self.project_description = wx.TextCtrl(self.project_settings_pane, -1, "")
        self.project_author_label = wx.StaticText(self.project_settings_pane, -1, "Author:", style=wx.ALIGN_RIGHT)
        self.project_author = wx.TextCtrl(self.project_settings_pane, -1, "")
        self.image_section_divider = wx.StaticLine(self.project_settings_pane, -1)
        self.project_image_label = wx.StaticText(self.project_settings_pane, -1, "Image:", style=wx.ALIGN_RIGHT)
        self.select_project_image = wx.Button(self.project_settings_pane, -1, "Select Image...")
        self.icon_bitmap = wx.StaticBitmap(self.project_settings_pane, -1, wx.Bitmap("images\\AddInDesktop48.png", wx.BITMAP_TYPE_ANY), style=wx.SIMPLE_BORDER)
        self.contents_tree = wx.TreeCtrl(self.project_items_pane, -1, style=wx.TR_HAS_BUTTONS|wx.TR_LINES_AT_ROOT|wx.TR_HIDE_ROOT|wx.TR_DEFAULT_STYLE|wx.RAISED_BORDER)
        self.bottom_buttons_spacer_panel = wx.Panel(self.bottom_buttons_pane, -1)
        self.open_folder = wx.Button(self.bottom_buttons_pane, -1, "Open Folder")
        self.save_button = wx.Button(self.bottom_buttons_pane, -1, "Save")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.SelectFolder, self.folder_button)
        self.Bind(wx.EVT_COMBOBOX, self.ComboBox, self.product_combo_box)
        self.Bind(wx.EVT_TEXT_ENTER, self.ProjectNameText, self.project_name)
        self.Bind(wx.EVT_TEXT, self.ProjectNameText, self.project_name)
        self.Bind(wx.EVT_TEXT_ENTER, self.ProjectVersionText, self.project_version)
        self.Bind(wx.EVT_TEXT, self.ProjectVersionText, self.project_version)
        self.Bind(wx.EVT_TEXT_ENTER, self.ProjectCompanyText, self.project_company)
        self.Bind(wx.EVT_TEXT, self.ProjectCompanyText, self.project_company)
        self.Bind(wx.EVT_TEXT_ENTER, self.ProjectDescriptionText, self.project_description)
        self.Bind(wx.EVT_TEXT, self.ProjectDescriptionText, self.project_description)
        self.Bind(wx.EVT_TEXT_ENTER, self.ProjectAuthorText, self.project_author)
        self.Bind(wx.EVT_TEXT, self.ProjectAuthorText, self.project_author)
        self.Bind(wx.EVT_BUTTON, self.SelectProjectImage, self.select_project_image)
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.BeginDrag, self.contents_tree)
        self.Bind(wx.EVT_TREE_END_DRAG, self.EndDrag, self.contents_tree)
        self.Bind(wx.EVT_TREE_DELETE_ITEM, self.DeleteItem, self.contents_tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.SelChanged, self.contents_tree)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.ChangeTab, self.tabs_notebook)
        self.Bind(wx.EVT_BUTTON, self.OpenFolder, self.open_folder)
        self.Bind(wx.EVT_BUTTON, self.SaveProject, self.save_button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AddinMakerWindow.__set_properties
        self.SetTitle("ArcGIS Python Add-In Wizard")
        self.SetMinSize(_msize)
        self.title_label.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.title_panel.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DHIGHLIGHT))
        self.product_combo_box.SetSelection(0)
        self.project_name_label.SetMinSize((72, 16))
        self.project_version_label.SetMinSize((72, 16))
        self.project_company_label.SetMinSize((72, 16))
        self.project_description_label.SetMinSize((72, 16))
        self.project_author_label.SetMinSize((72, 16))
        self.project_image_label.SetMinSize((72, 16))
        self.contents_tree.SetMinSize((200, 484))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AddinMakerWindow.__do_layout
        full_window_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        bottom_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        splitter_sizer = wx.BoxSizer(wx.HORIZONTAL)
        items_sizer = wx.BoxSizer(wx.HORIZONTAL)
        item_property_sizer = wx.BoxSizer(wx.VERTICAL)
        fields_sizer = wx.BoxSizer(wx.VERTICAL)
        properties_rows_holder = wx.StaticBoxSizer(self.properties_rows_holder_staticbox, wx.VERTICAL)
        project_bitmap_display_sizer = wx.BoxSizer(wx.HORIZONTAL)
        properties_rows = wx.BoxSizer(wx.VERTICAL)
        project_image_sizer = wx.BoxSizer(wx.HORIZONTAL)
        project_author_sizer = wx.BoxSizer(wx.HORIZONTAL)
        project_description_sizer = wx.BoxSizer(wx.HORIZONTAL)
        project_company_sizer = wx.BoxSizer(wx.HORIZONTAL)
        project_version_sizer = wx.BoxSizer(wx.HORIZONTAL)
        project_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        product_sizer = wx.BoxSizer(wx.HORIZONTAL)
        folder_sizer = wx.BoxSizer(wx.HORIZONTAL)
        logo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        title_sizer.Add(self.title_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 8)
        self.title_panel.SetSizer(title_sizer)
        main_sizer.Add(self.title_panel, 0, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        main_sizer.Add(self.title_divider_line, 0, wx.EXPAND, 0)
        logo_sizer.Add(self.logo_bitmap, 0, wx.TOP, 8)
        self.logo_panel.SetSizer(logo_sizer)
        splitter_sizer.Add(self.logo_panel, 0, wx.EXPAND, 0)
        folder_sizer.Add(self.folder_label, 0, wx.ALIGN_CENTER_VERTICAL, 8)
        folder_sizer.Add(self.folder_button, 1, wx.EXPAND, 8)
        fields_sizer.Add(folder_sizer, 0, wx.ALL|wx.EXPAND, 4)
        product_sizer.Add(self.product_label, 0, wx.ALIGN_CENTER_VERTICAL, 3)
        product_sizer.Add(self.product_combo_box, 0, 0, 3)
        fields_sizer.Add(product_sizer, 0, wx.ALL|wx.EXPAND, 4)
        fields_sizer.Add(self.static_line_1, 0, wx.ALL|wx.EXPAND, 8)
        project_name_sizer.Add(self.project_name_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_name_sizer.Add(self.project_name, 1, wx.EXPAND, 0)
        properties_rows.Add(project_name_sizer, 1, wx.EXPAND, 0)
        project_version_sizer.Add(self.project_version_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_version_sizer.Add(self.project_version, 1, wx.EXPAND, 0)
        properties_rows.Add(project_version_sizer, 1, wx.EXPAND, 0)
        project_company_sizer.Add(self.project_company_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_company_sizer.Add(self.project_company, 1, wx.EXPAND, 0)
        properties_rows.Add(project_company_sizer, 1, wx.EXPAND, 0)
        project_description_sizer.Add(self.project_description_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_description_sizer.Add(self.project_description, 1, wx.EXPAND, 0)
        properties_rows.Add(project_description_sizer, 1, wx.EXPAND, 0)
        project_author_sizer.Add(self.project_author_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_author_sizer.Add(self.project_author, 1, wx.EXPAND, 0)
        properties_rows.Add(project_author_sizer, 1, wx.EXPAND, 0)
        properties_rows.Add(self.image_section_divider, 0, wx.ALL|wx.EXPAND, 2)
        project_image_sizer.Add(self.project_image_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2)
        project_image_sizer.Add(self.select_project_image, 0, 0, 0)
        properties_rows.Add(project_image_sizer, 1, wx.EXPAND, 3)
        properties_rows_holder.Add(properties_rows, 0, wx.EXPAND, 0)
        project_bitmap_display_sizer.Add(self.icon_bitmap, 0, wx.TOP, 3)
        properties_rows_holder.Add(project_bitmap_display_sizer, 1, wx.LEFT|wx.EXPAND, 80)
        fields_sizer.Add(properties_rows_holder, 0, wx.EXPAND, 0)
        self.project_settings_pane.SetSizer(fields_sizer)
        items_sizer.Add(self.contents_tree, 0, wx.EXPAND, 0)
        self.item_property_panel.SetSizer(item_property_sizer)
        items_sizer.Add(self.item_property_panel, 1, wx.EXPAND, 0)
        self.project_items_pane.SetSizer(items_sizer)
        self.tabs_notebook.AddPage(self.project_settings_pane, "Project Settings")
        self.tabs_notebook.AddPage(self.project_items_pane, "Add-In Contents")
        splitter_sizer.Add(self.tabs_notebook, 1, wx.EXPAND, 4)
        content_sizer.Add(splitter_sizer, 1, wx.EXPAND, 4)
        self.propsheet_panel.SetSizer(content_sizer)
        main_sizer.Add(self.propsheet_panel, 1, wx.EXPAND, 0)
        bottom_buttons_sizer.Add(self.bottom_buttons_spacer_panel, 1, wx.EXPAND, 0)
        bottom_buttons_sizer.Add(self.open_folder, 0, wx.ALL, 2)
        bottom_buttons_sizer.Add(self.save_button, 0, wx.ALL, 2)
        self.bottom_buttons_pane.SetSizer(bottom_buttons_sizer)
        main_sizer.Add(self.bottom_buttons_pane, 0, wx.EXPAND, 4)
        self.full_app_panel.SetSizer(main_sizer)
        full_window_sizer.Add(self.full_app_panel, 1, wx.ALL|wx.EXPAND, 1)
        self.SetSizer(full_window_sizer)
        full_window_sizer.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def SelectFolder(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `SelectFolder' not implemented!"
        event.Skip()

    def ComboBox(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ComboBox' not implemented!"
        event.Skip()

    def ProjectNameText(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ProjectNameText' not implemented!"
        event.Skip()

    def ProjectVersionText(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ProjectVersionText' not implemented!"
        event.Skip()

    def ProjectCompanyText(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ProjectCompanyText' not implemented!"
        event.Skip()

    def ProjectDescriptionText(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ProjectDescriptionText' not implemented!"
        event.Skip()

    def ProjectAuthorText(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ProjectAuthorText' not implemented!"
        event.Skip()

    def SelectProjectImage(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `SelectProjectImage' not implemented!"
        event.Skip()

    def BeginDrag(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `BeginDrag' not implemented!"
        event.Skip()

    def EndDrag(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `EndDrag' not implemented!"
        event.Skip()

    def DeleteItem(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `DeleteItem' not implemented!"
        event.Skip()

    def SelChanged(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `SelChanged' not implemented!"
        event.Skip()

    def ChangeTab(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `ChangeTab' not implemented!"
        event.Skip()

    def OpenFolder(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `OpenFolder' not implemented!"
        event.Skip()

    def SaveProject(self, event): # wxGlade: AddinMakerWindow.<event_handler>
        print "Event handler `SaveProject' not implemented!"
        event.Skip()

# end of class AddinMakerWindow


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    addin_window = AddinMakerWindow(None, -1, "")
    app.SetTopWindow(addin_window)
    addin_window.Show()
    app.MainLoop()
