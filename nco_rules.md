<function>
  <name>ncrename</name>
  <function>ncrename -v sst,sst_new oisst_monthly.nc</function>
  <description>使用nco修改netcdf数据中的变量名。例如，将变量名sst修改为sst_new。</description>
</function>
<function>
  <name>ncatted</name>
  <function>ncatted -O -a missing_value, MITVAR,o,f,0 dasilva94_monthly_sst.nc; ncatted -O -a _FillValue, MITVAR,o,f,0 dasilva94_monthly_sst.nc</function>
  <description>使用nco修改netcdf文件中属性的名称。例如，将netcdf文件中的miss_value和_FillValue更改为零。</description>
</function>
<function>
  <name>cdo chname</name>
  <function>cdo chname,sst_new,sst_renew oisst_monthly.nc oisst_monthly_renew.nc</function>
  <description>使用cdo修改netcdf数据中的变量名。例如，在已将sst修改为sst_new的基础上，将其修改为sst_renew。</description>
</function>
<function>
  <name>wget</name>
  <function>wget -o./get -c -nH -c -r -A nc "https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/${year}${month}/${filename}"</function>
  <description>通过写shell脚本使用wget从ftp或者网页直接下载数据。根据链接有规则命名的属性进行循环迭代下载多个文件。</description>
</function>
<function>
  <name>cdo enssum</name>
  <function>cdo enssum file1 file2 out.nc; cdo enssum *_sst.nc out.nc</function>
  <description>使用cdo对多个netcdf文件进行求和计算。</description>
</function>
<function>
  <name>cdo remapcon</name>
  <function>cdo remapcon,r180x90 pr.nc pr_regrid_2x2.nc</function>
  <description>使用cdo对netcdf数据进行守恒插值（适用于降水数据）。</description>
</function>
<function>
  <name>cdo remapbic</name>
  <function>cdo remapbic,r144x73 in.nc out_interp.nc</function>
  <description>使用cdo对netcdf数据进行双线性插值。</description>
</function>
<function>
  <name>cdo setcalendar</name>
  <function>cdo setcalendar,standard ua_day_EC-Earth3_data.nc ua_day_EC-Earth3_data_stand.nc</function>
  <description>使用cdo修改netcdf数据calendar的类型。</description>
</function>
<function>
  <name>cdo mergetime</name>
  <function>cdo mergetime GPM*.nc GPM-2004-05-07.nc</function>
  <description>使用cdo将多个netcdf文件按照时间维度进行合并。</description>
</function>
<function>
  <name>cdo lowpass</name>
  <function>cdo lowpass,0.1 sst.anomaly.nc out.nc</function>
  <description>对于月平均的netcdf数据进行10个月的低通滤波。注意数据中不能存在nan值或者缺测值。</description>
</function>
<function>
  <name>cdo bandpass</name>
  <function>cdo bandpass,365/60,365/30 sst.day.ano.nc out.nc</function>
  <description>对于日平均的netcdf数据进行30 - 60天的带通滤波。注意数据中不能存在nan值或者缺测值。</description>
</function>
<function>
  <name>cdo setmissval (nan)</name>
  <function>cdo setmissval,nan input.nc output.nc</function>
  <description>使用cdo将netcdf数据中正常的数据转换为Nan值。</description>
</function>
<function>
  <name>cdo setmissval (0)</name>
  <function>cdo setmissval,0 input.nc output.nc</function>
  <description>使用cdo将netcdf数据中Nan值转化为其他值（这里是0）。</description>
</function>
