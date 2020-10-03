class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #Switch element[0] with element[len-1], element[1] with element[len-2]
        #[1,0,0,1,0] Stop and not include element 3 (5)
        #[1,1,1,1,0,1,0] Stop and not include element 4 (7)
        #[1,0,1,0,1,1,1,0,0,1,0] Stop and not include element 6 (11)
        # for lists with odd numbers of elements len+1 / 2 is the element to Stop at and not move?
        #[0,1,1,0] 4 Stop at and include len/2 element
        
        #List has been flipped with python list's built in reversed function
        flipped_list,tmp_list,counter = [],[],0
        for i in A:
            tmp_list = reversed(i)
            flipped_list.insert(counter,tmp_list)
            counter += 1
        
        reciprocal_list,locallist_counter,reciprocallist_counter = [],0,0
        for i in flipped_list:
            local_list = []
            for j in i:
                if j == 0:
                    local_list.insert(locallist_counter,1)
                elif j == 1:
                    local_list.insert(locallist_counter,0)
                locallist_counter += 1
            reciprocal_list.insert(reciprocallist_counter,local_list)
            reciprocallist_counter += 1
        return reciprocal_list
