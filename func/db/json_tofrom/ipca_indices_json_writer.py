#!/usr/bin/env python3
'''
json_writer_ipca_indices.py
'''
import func.db.json_tofrom.general_json_reader_writer as jsongen

json_filename = 'ipca_indices_realestaterentsystem.json'
year_month_ipca_dict = {}
year_month_ipca_dict[2004] = [ 0.76, 0.61, 0.47, 0.37, 0.51, 0.71, 0.91, 0.69, 0.33, 0.44, 0.69, 0.86]
year_month_ipca_dict[2005] = [ 0.58, 0.59, 0.61, 0.87, 0.49, -0.02, 0.25, 0.17, 0.35, 0.75, 0.55, 0.36]
year_month_ipca_dict[2006] = [ 0.59, 0.41, 0.43, 0.21, 0.1, -0.21, 0.19, 0.05, 0.21, 0.33, 0.31, 0.48]
year_month_ipca_dict[2007] = [ 0.44, 0.44, 0.37, 0.25, 0.28, 0.28, 0.24, 0.47, 0.18, 0.3, 0.38, 0.74]
year_month_ipca_dict[2008] = [ 0.54, 0.49, 0.48, 0.55, 0.79, 0.74, 0.53, 0.28, 0.26, 0.45, 0.36, 0.28]
year_month_ipca_dict[2009] = [ 0.48, 0.55, 0.2, 0.48, 0.47, 0.36, 0.24, 0.15, 0.24, 0.28, 0.41, 0.37]
year_month_ipca_dict[2010] = [ 0.75, 0.78, 0.52, 0.57, 0.43, 0, 0.01, 0.04, 0.45, 0.75, 0.83, 0.63]
year_month_ipca_dict[2011] = [ 0.83, 0.8, 0.79, 0.77, 0.47, 0.15, 0.16, 0.37, 0.53, 0.43, 0.52, 0.5]
year_month_ipca_dict[2012] = [ 0.56, 0.45, 0.21, 0.64, 0.36, 0.08, 0.43, 0.41, 0.57, 0.59, 0.6, 0.79]
year_month_ipca_dict[2013] = [ 0.86, 0.6, 0.47, 0.55, 0.37, 0.26, 0.03, 0.24, 0.35, 0.57, 0.54, 0.92]
year_month_ipca_dict[2014] = [ 0.55, 0.69, 0.92, 0.67, 0.46, 0.4, 0.01, 0.25, 0.57, 0.42, 0.51, 0.78]
year_month_ipca_dict[2015] = [ 1.24, 1.22, 1.32, 0.71, 0.74, 0.79, 0.62, 0.22, 0.54, 0.82, 1.01, 0.96]
year_month_ipca_dict[2016] = [ 1.27, 0.9, 0.43, 0.61, 0.78, 0.35, 0.52, 0.44, 0.08, 0.26, 0.18, 0.3]
year_month_ipca_dict[2017] = [ 0.38, 0.33, 0.25, 0.14, 0.31, -0.23, 0.24, 0.19, 0.16, 0.42, 0.28, 0.44]
year_month_ipca_dict[2018] = [ 0.29, 0.32, 0.09, 0.22, 0.4, 1.26, 0.33, -0.09, 0.48, 0.45, -0.21, 0.15]
year_month_ipca_dict[2019] = [ 0.32, 0.43, 0.75, 0.57, 0.13, 0.01, 0.19, 0.11, -0.04, 0.1, None, None]

jsongen.write_pythondata_to_jsondbfolder(year_month_ipca_dict, json_filename)
