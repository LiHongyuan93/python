# 用于生成分页代码。
class PageUtil(object):
    # 分页table的css 类名
    table_class_name = "pageTable";

    # 功能：得到当前页分页信息。Map key totalPage 共计多少页，firstRecord 本页第一条记录序号，lastRecord 本页最后一条记录序号。<br/>
    # 如果当前页数大于了最后一个页码，则返回有效记录之内的序号。
    # @param currentPage 当前要显示第几页
    # @param recordCountOfOnePage 每天显示多少条。
    # @param recordCount 共计多少条记录。
    def get_current_page_info(self, current_page: int, record_count_of_page: int, record_count: int):
        # 参数无效
        if current_page < 1 or record_count_of_page < 1 or record_count < 1:
            return None
        # 总页数;
        totalPage = record_count // record_count_of_page
        if record_count % record_count_of_page != 0:
            totalPage = (record_count // record_count_of_page) + 1
        # 计算出来当页第一条和最后一条记录序号,做了页数超出的处理。
        firstRecord = ((current_page - 1) * record_count_of_page) + 1
        if firstRecord >= record_count:
            firstRecord = record_count
        lastRecord = current_page * record_count_of_page
        if lastRecord >= record_count:
            lastRecord = record_count;
        return totalPage, firstRecord, lastRecord

    # 功能：得到Ajax分页代码。分页代码table的样式class="+tableClassName+"，可以对其进行样式设计,采用第一种分页模式。<br/>
    # 原理：点击任何一页超链接会调用functionName JS函数，并且会将currentPage传入到函数中，其他ajax处理直接在functionName中操作即可。<br/>
    # @param functionName 点击上一页或者其他起码时触发的JS函数名，会自动将currentPage传入函数。<br/>
    # @param currentPage 当前为第几页
    # @param pageCount 一共有多少页
    # @param recordCount 共有多少条记录，只是用来展示不参与运算。
    def get_ajax_page_html(self, functionName: str, currentPage: int, pageCount: int, recordCount: int):
        output = ["<table class=" + self.table_class_name + " align=center width=100% cellspacing=0 cellpadding=0 >\n",
                  "<tr>\n", "<td align=center >共" + str(recordCount) + "个</td>\n"]
        if currentPage <= 1:
            output.append("<td align=center ><div align=left>首页</div></td>\n")
            output.append("<td  align=center ><div align=left>上一页</div></td>\n")
        else:
            output.append(
                "<td align=center > <div align=left><a href='javascript:void(0);' onclick=\"" + functionName + "(1);\">首页</a></div></td>\n")
            output.append(
                "<td align=center> <div align=left><a href='javascript:void(0);' onclick=\"" + functionName + "(" + str(
                    currentPage - 1) + ");\">上一页</a></div></td>\n")

        if currentPage != pageCount and pageCount != 0:
            output.append(
                "<td align=center > <div align=left><a href='javascript:void(0);' onclick=\"" + functionName + "(" + str(
                    currentPage + 1) + ");\">下一页</a></div></td>\n")
            output.append(
                "<td align=center> <div align=left><a href='javascript:void(0);' onclick=\"" + functionName + "(" + str(
                    pageCount) + ");\">尾页</a></div></td>\n")
        else:
            output.append("<td align=center> <div align=left>下一页</div></td>\n")
            output.append("<td align=center> <div align=left>尾页</div></td>\n")
        output.append(
            "<td align=center> <div align=left>当前第" + str(currentPage) + "页/共" + str(pageCount) + "页</div></td>\n")
        output.append("<td align=center  class=fContent><div align=left>到第\n")
        if pageCount == 0:
            output.append("<select name=currentPage disabled>\n")
        else:
            output.append("<select name=currentPage id=\"currentPage\" onChange='" + functionName + "(this.value);'>\n")
        # 分页页码
        i = 1
        while i <= pageCount:
            if i == currentPage:
                output.append("<option value=" + str(i) + " selected>" + str(i) + "</option>\n")
            else:
                output.append("<option value=" + str(i) + ">" + str(i) + "</option>\n")
            i += 1
        output.append("</select>页\n")
        output.append("</tr></table>\n")
        return ''.join(output);
